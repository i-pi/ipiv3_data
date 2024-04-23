import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

#--------------------------------------------------------
plt.rc("font", **{"family": "sans-serif", "sans-serif": ["Arial"]})
tick_major_size = 10
tick_minor_size = 7
labelsize = 20
fontsize = 18
legend_fontsize = 15

plt.rcParams["font.size"] = fontsize
plt.rc("axes", linewidth=2, labelpad=10)
#plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"
plt.rc("xtick.major", size=tick_major_size, width=2)
plt.rc("xtick.minor", size=tick_minor_size, width=2)
plt.rc("ytick.major", size=tick_major_size, width=2)
plt.rc("ytick.minor", size=tick_minor_size, width=2)
#--------------------------------------------------------
figsize=(7,5)

ha2ev = 27.211386
obs = np.loadtxt("QQbar")
pots = np.loadtxt("POTS") * ha2ev

fig, ax = plt.subplots(1, 1, figsize=figsize, constrained_layout=True)
timeline = np.arange(len(pots)) * 0.01 - 12.5  # shift to show an "interesting" part
color_v = "k"  #'#FF3000'
color_q = "k"  # '#0000C0'
for i in range(5):
    ax.plot(timeline, (pots[:, i] - pots.mean()), color=f"C{i}", alpha=0.5, lw=1)
ax.set_xlim(0, 1.5)
ax.set_ylim(-4.0, 2.5)
ax.set_xlabel(r"$t$ (ps)")
ax.set_ylabel(r"($V^{(k)}-\langle{V}\rangle)$ (eV)")

# Create a second axes for the different y scale
ax2 = ax.twinx()
# Adjust the data for the blue line by shrinking its scale
scaled_obs = obs / 5
ax2.plot(timeline, scaled_obs, color=color_q, lw=0.75, zorder=1)
ax2.axhline(y=0, lw=0.5, color=color_q, ls="--")
ax2.set_ylim(-3.4, 2.5)
ticks_real = ax2.get_yticks() * 5  # Scale the tick values back to original
ax2.set_yticklabels([f"{tick:.1f}" for tick in ticks_real])
ax2.set_ylabel(r"$(n_{\mathrm{s}}-\bar{n})$")

ax.spines["left"].set_color(color_v)
ax.yaxis.label.set_color(color_v)
ax.tick_params(axis="y", colors=color_v)


ax2.spines["left"].set_color(color_v)
ax2.spines["right"].set_color(color_q)
ax2.yaxis.label.set_color(color_q)
ax2.tick_params(axis="y", colors=color_q)

ax.set_zorder(ax2.get_zorder() + 1)  # Makes ax in the front
ax.patch.set_visible(False)  # Makes ax background transparent

# Draw a rectangle with a background color that covers the whole bbox
background_patch = mpl.patches.Rectangle(
    (0.42, 0.42), 1, 1, color="white", alpha=0.5, transform=ax.transAxes, zorder=3
)
ax.add_patch(background_patch)

inset_ax = ax.inset_axes([0.55, 0.55, 0.43, 0.43])
inset_ax.plot(
    pots[:, 1] - pots.mean(axis=1), obs, "k,", alpha=0.2, markersize=1, rasterized=True
)
inset_ax.set_xlabel(r"($V^{(1)}-\bar{V})$ (eV)", fontsize=8, labelpad=-3)
inset_ax.set_ylabel(r"$(n_{\mathrm{s}}-\bar{n})$", fontsize=8, labelpad=-10)
inset_ax.tick_params(labelsize=8)
inset_ax.xaxis.set_label_position("bottom")
inset_ax.xaxis.set_ticks_position("bottom")
inset_ax.set_xlim(-0.4, -0.1)


fig.savefig("ensemblemu-trajectory.pdf")


#------------------------------------------------------------
figsize=(6,3)
kt = 0.00091837535 * ha2ev
h = (pots - pots.mean(axis=1)[:, np.newaxis]) / kt
w = np.exp(-h)
direct_cs = np.cumsum(w * obs[:, np.newaxis], axis=0) / np.cumsum(w, axis=0)
cw = np.cumsum(h * 0 + 1, axis=0)
cavg = np.cumsum(obs, axis=0) / cw[:, 0]
cea_cs = np.cumsum(obs[:, np.newaxis], axis=0) / cw - (
    np.cumsum(h * obs[:, np.newaxis], axis=0) / cw
    - np.cumsum(h, axis=0) / cw * np.cumsum(obs[:, np.newaxis], axis=0) / cw
)


#fig, ax = plt.subplots(2, 1, figsize=figsize, sharex=True, constrained_layout=True)
for iplot in range(2):
 fig, ax = plt.subplots(1, figsize=figsize, constrained_layout=True)
 timeline = np.arange(len(pots)) * 0.01
 if iplot==0:
  for i in range(5):
     ax.semilogx(timeline, direct_cs[:, i], "-", color=f"C{i}")
 else:
  for i in range(5):
     ax.semilogx(timeline, cea_cs[:, i], color=f"C{i}")
 ax.semilogx(timeline, cavg, "k--")
 ax.set_xlabel(r"$t$ (ps)")
 ax.set_ylabel(r"$\langle n_{\mathrm{s}}-\bar{n}\rangle_k$")
 if iplot==0:
   ax.text(1e-2, -10, "reweight")
 else:
   ax.text(1e-2, -10, "CEA")
 ax.set_ylim(-11, 2)
 
 fig.savefig("ensemblemu-reweight_{}.pdf".format(iplot))

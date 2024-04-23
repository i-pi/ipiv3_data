import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
# Define format
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

fig,ax = plt.subplots(figsize=(6,5))

fig, ax = plt.subplots(1, figsize=(7,5), constrained_layout=True)
x = np.geomspace(1e-5, 1e2, 100)

ax.loglog(x, 86.4e3*1e-6/x, ':', c='gray', label=r"$\tau_\mathrm{O}=0$ (ideal)")
for e, c, t in zip([-5,-3,-1, 1], ["#0000B0", "#401090", "#802040", "#FF4010"], ["10^{-2}$ ms","10^0$ ms", "10^2$ ms", "10^4$ ms"]):
    ax.loglog(x, 86.4e3*1e-6/(x+10.0**e), '--', c=c, label=r"$\tau_\mathrm{O}="+t)

ax.fill_between(x, 86.4e3*1e-6/(x+2e-3), 86.4e3*1e-6/(x+2e-2), color="gray", alpha=0.2, lw=0)
ax.fill_between(x, 86.4e3*1e-6/(x+5e-3), 86.4e3*1e-6/(x+1e-2), color="k", alpha=0.3, lw=0, label=r"typical i-PI MD")

ax.text(10, 5e-4, "ab initio", ha="center")
ax.text(0.03, 5e-4, "MLIP", ha="center")
ax.text(5e-5, 5e-4, "forcefields", ha="center")
ax.legend(labelspacing=0.1)
ax.set_xlabel(r"Force evaluation time (s)")
ax.set_ylabel(r"Simulation throughput  (ns/day)")
fig.savefig("simple-overhead-scheme.pdf")

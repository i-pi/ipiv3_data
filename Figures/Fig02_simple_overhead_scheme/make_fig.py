import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

fig, ax = plt.subplots(1,1, figsize=(4,3), constrained_layout=True)
x = np.geomspace(1e-5, 1e2, 100)

ax.loglog(x, 86.4e3*1e-6/x, ':', c='gray', label=r"ideal, $\tau_\mathrm{O}=0$")
for e, c, t in zip([-5,-3,-1, 1], ["#0000B0", "#401090", "#802040", "#FF4010"], ["0.01$ ms","1$ ms", "100$ ms", "10$ s"]):
    ax.loglog(x, 86.4e3*1e-6/(x+10.0**e), '--', c=c, label=r"$\tau_\mathrm{O}="+t)

ax.fill_between(x, 86.4e3*1e-6/(x+2e-3), 86.4e3*1e-6/(x+2e-2), color="gray", alpha=0.2, lw=0)
ax.fill_between(x, 86.4e3*1e-6/(x+5e-3), 86.4e3*1e-6/(x+1e-2), color="k", alpha=0.3, lw=0, label=r"typical i-PI MD")

ax.text(10, 5e-4, "ab initio", ha="center")
ax.text(0.03, 5e-4, "MLIP", ha="center")
ax.text(5e-5, 5e-4, "forcefields", ha="center")
ax.legend(labelspacing=0.1)
ax.set_xlabel(r"force evaluation time / s")
ax.set_ylabel(r"simulation throughput / (ns/day)")
fig.savefig("simple-overhead-scheme.pdf")

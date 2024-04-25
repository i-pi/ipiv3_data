# %%
import numpy as np
import matplotlib.pyplot as plt

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

def one_n(x, offset=0):
    return (1.0 / x) * offset


# %%
folder = "./"
ipi_cpu = np.loadtxt(f"{folder}/timing_ipi_cpu.out")
ipi_gpu = np.loadtxt(f"{folder}/timing_ipi_gpu.out")

lammps_cpu = np.loadtxt(f"{folder}/timing_lammps_cpu.out")
lammps_gpu = np.loadtxt(f"{folder}/timing_lammps_gpu.out")


# %%
ipi_32beads_cpu = {}
ipi_32beads_gpu = {}
for i in [1, 2, 4, 8]:
    ipi_32beads_cpu[f"{i}_lammps"] = np.loadtxt(
        f"{folder}/timing_ipi-32_beads-{i}_lammps_cpu.out"
    )
    ipi_32beads_gpu[f"{i}_lammps"] = np.loadtxt(
        f"{folder}/timing_ipi-32_beads-{i}_lammps_gpu.out"
    )

ipi_32beads_cpu[f"16_lammps"] = np.loadtxt(
    f"{folder}/timing_ipi-32_beads-16_lammps_cpu.out"
)
ipi_32beads_cpu[f"32_lammps"] = np.loadtxt(
    f"{folder}/timing_ipi-32_beads-32_lammps_cpu.out"
)

# %%


# Figure 1
fig, axs = plt.subplots(1,  figsize=(6, 5))# 2, 1, sharex=True, tight_layout=True, figsize=(10, 12))
axs.set_aspect(0.8)

# Plot for CPUs on the first axis
axs.loglog(
    lammps_cpu[:, 0],
    lammps_cpu[:, 1],
    ls="--",
    marker="o",
    color="red",
    label="LAMMPS, CPU",
)
axs.loglog(
    lammps_gpu[:, 0],
    lammps_gpu[:, 1],
    ls="--",
    marker="o",
    color="blue",
    label="LAMMPS, GPU",
)
axs.loglog(
    ipi_cpu[:, 0], ipi_cpu[:, 1], ls="-", marker="o", color="red", label="i-PI, CPU"
)
axs.loglog(
    ipi_gpu[:, 0], ipi_gpu[:, 1], ls="-", marker="o", color="blue", label="i-PI, GPU"
)

x = np.arange(1, 500)
axs.loglog(x, one_n(x, offset=np.exp(-2.5)), ls=":", c="grey", lw=2)
axs.loglog(x, one_n(x, offset=np.exp(2.2)), ls=":", c="grey", lw=2)
axs.loglog(x, one_n(x, offset=np.exp(-0.20)), ls=":", c="grey", lw=2)
axs.loglog(x, one_n(x, offset=np.exp(50)), ls=":", c="grey", lw=2, label="1/n")
axs.set_ylim(0.009, 15.0)

# ax1.set_xlabel('nCPU,nGPU')
axs.set_ylabel("Time / Step (s)", size=labelsize)
axs.set_xlabel("nCPU,nGPU", size=labelsize)
axs.legend(fontsize=legend_fontsize)
# ax1.grid(True, which="both", ls="--")

axs.text(0.75, 0.01, "MD", transform=axs.transAxes, weight="bold")
fig.savefig("deepmd-timing_1.pdf", dpi=300)

# Figure 2
fig, axs = plt.subplots(1,  figsize=(6, 5))# 2, 1, sharex=True, tight_layout=True, figsize=(10, 12))
#fig, axs = plt.subplots(1)# 2, 1, sharex=True, tight_layout=True, figsize=(10, 12))
axs.set_aspect(0.8)


axs.loglog(
    ipi_32beads_cpu["1_lammps"][:, 0],
    ipi_32beads_cpu["1_lammps"][:, 1],
    ls="-",
    marker="o",
    color="red",
    alpha=0.2,
)
axs.loglog(
    ipi_32beads_cpu["2_lammps"][:, 0] * 2,
    ipi_32beads_cpu["2_lammps"][:, 1],
    ls="-",
    marker="o",
    color="red",
    alpha=0.4,
)
axs.loglog(
    ipi_32beads_cpu["4_lammps"][:, 0] * 4,
    ipi_32beads_cpu["4_lammps"][:, 1],
    ls="-",
    marker="o",
    color="red",
    alpha=0.8,
)
axs.loglog(
    ipi_32beads_cpu["8_lammps"][:, 0] * 8,
    ipi_32beads_cpu["8_lammps"][:, 1],
    ls="-",
    marker="o",
    color="red",
    alpha=1,
)

axs.loglog(
    ipi_32beads_gpu["1_lammps"][:, 0],
    ipi_32beads_gpu["1_lammps"][:, 1],
    ls="-",
    marker="o",
    color="blue",
    alpha=0.2,
)
axs.loglog(
    ipi_32beads_gpu["2_lammps"][:, 0] * 2,
    ipi_32beads_gpu["2_lammps"][:, 1],
    ls="-",
    marker="o",
    color="blue",
    alpha=0.4,
)
axs.loglog(
    ipi_32beads_gpu["4_lammps"][:, 0] * 4,
    ipi_32beads_gpu["4_lammps"][:, 1],
    ls="-",
    marker="o",
    color="blue",
    alpha=0.8,
)
axs.loglog(
    ipi_32beads_gpu["8_lammps"][ 0] * 8,
    ipi_32beads_gpu["8_lammps"][ 1],
    ls="-",
    marker="o",
    color="blue",
    alpha=1,
)


# Plot for GPUs on the second axis
# ax2.loglog(n, time_lammps_gpu, marker='s', label='LAMMPS, GPU')
# ax2.loglog(n, time_ipi_gpu, marker='x', label='i-PI, GPU')
axs.set_ylabel("Time / Step (s)", size=labelsize)
axs.set_xlabel("nCPU,nGPU", size=labelsize)
axs.legend(fontsize=legend_fontsize)
# ax2.grid(True, which="both", ls="--")

x = np.arange(1, 500)
axs.loglog(x, one_n(x, offset=np.exp(1.55)), ls=":", c="grey", lw=2)
axs.loglog(x, one_n(x, offset=np.exp(3.32)), ls=":", c="grey", lw=2)
axs.loglog(x, one_n(x, offset=np.exp(5.80)), ls=":", c="grey", lw=2)
axs.set_ylim(0.3, 410)

x = np.arange(1, 500)
y = np.ones(len(x)) * 10000
axs.loglog(x, y, ls="-", color="grey", alpha=0.2, label="1 task", lw=4)
axs.loglog(x, y, ls="-", color="grey", alpha=0.4, label="2 task", lw=4)
axs.loglog(x, y, ls="-", color="grey", alpha=0.8, label="4 task", lw=4)
axs.loglog(x, y, ls="-", color="grey", alpha=1, label="8 task", lw=4)
axs.legend()

axs.text(0.75, 0.01, "PIMD-32", transform=axs.transAxes, weight="bold")

fig.savefig("deepmd-timing_2.pdf", dpi=300)

# %%

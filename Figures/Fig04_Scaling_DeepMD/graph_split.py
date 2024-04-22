# %%
import numpy as np
import matplotlib.pyplot as plt


# Format
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
for i in [1, 2, 4, 8, 16]:
    ipi_32beads_cpu[f"{i}_lammps"] = np.loadtxt(
        f"{folder}/timing_ipi-32_beads-{i}_lammps_cpu.out"
    )
    ipi_32beads_gpu[f"{i}_lammps"] = np.loadtxt(
        f"{folder}/timing_ipi-32_beads-{i}_lammps_gpu.out"
    )

ipi_32beads_cpu[f"32_lammps"] = np.loadtxt(
    f"{folder}/timing_ipi-32_beads-32_lammps_cpu.out"
)

# %%



# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, tight_layout=True, figsize=(10, 12))
plt.rcParams["xtick.labelsize"] = 22  # Size of numbers on the x-axis
plt.rcParams["ytick.labelsize"] = 22  # Size of numbers on the y-axis
plt.rcParams["font.size"] = 22

# Plot for CPUs on the first axis
ax1.loglog(
    lammps_cpu[:, 0],
    lammps_cpu[:, 1],
    ls="--",
    marker="o",
    color="red",
    label="LAMMPS, CPU",
)
ax1.loglog(
    lammps_gpu[:, 0],
    lammps_gpu[:, 1],
    ls="--",
    marker="o",
    color="blue",
    label="LAMMPS, GPU",
)
ax1.loglog(
    ipi_cpu[:, 0], ipi_cpu[:, 1], ls="-", marker="o", color="red", label="i-PI, CPU"
)
ax1.loglog(
    ipi_gpu[:, 0], ipi_gpu[:, 1], ls="-", marker="o", color="blue", label="i-PI, GPU"
)

x = np.arange(1, 500)
ax1.loglog(x, one_n(x, offset=np.exp(-2.5)), ls=":", c="grey", lw=2)
ax1.loglog(x, one_n(x, offset=np.exp(2.2)), ls=":", c="grey", lw=2)
ax1.loglog(x, one_n(x, offset=np.exp(-0.20)), ls=":", c="grey", lw=2)
ax1.loglog(x, one_n(x, offset=np.exp(50)), ls=":", c="grey", lw=2, label="1/n")
ax1.set_ylim(0.009, 15.0)

# ax1.set_xlabel('nCPU,nGPU')
ax1.set_ylabel("Time/Step [s]", size=22)
ax1.legend()
# ax1.grid(True, which="both", ls="--")

ax2.loglog(
    ipi_32beads_cpu["1_lammps"][:, 0],
    ipi_32beads_cpu["1_lammps"][:, 1],
    ls="-",
    marker="o",
    color="red",
    alpha=0.2,
)
ax2.loglog(
    ipi_32beads_cpu["2_lammps"][:, 0] * 2,
    ipi_32beads_cpu["2_lammps"][:, 1],
    ls="-",
    marker="o",
    color="red",
    alpha=0.4,
)
ax2.loglog(
    ipi_32beads_cpu["4_lammps"][:, 0] * 4,
    ipi_32beads_cpu["4_lammps"][:, 1],
    ls="-",
    marker="o",
    color="red",
    alpha=0.8,
)
ax2.loglog(
    ipi_32beads_cpu["8_lammps"][:, 0] * 8,
    ipi_32beads_cpu["8_lammps"][:, 1],
    ls="-",
    marker="o",
    color="red",
    alpha=1,
)

ax2.loglog(
    ipi_32beads_gpu["1_lammps"][:, 0],
    ipi_32beads_gpu["1_lammps"][:, 1],
    ls="-",
    marker="o",
    color="blue",
    alpha=0.2,
)
ax2.loglog(
    ipi_32beads_gpu["2_lammps"][:, 0] * 2,
    ipi_32beads_gpu["2_lammps"][:, 1],
    ls="-",
    marker="o",
    color="blue",
    alpha=0.4,
)
ax2.loglog(
    ipi_32beads_gpu["4_lammps"][:, 0] * 4,
    ipi_32beads_gpu["4_lammps"][:, 1],
    ls="-",
    marker="o",
    color="blue",
    alpha=0.8,
)
ax2.loglog(
    ipi_32beads_gpu["8_lammps"][:, 0] * 8,
    ipi_32beads_gpu["8_lammps"][:, 1],
    ls="-",
    marker="o",
    color="blue",
    alpha=1,
)


# Plot for GPUs on the second axis
# ax2.loglog(n, time_lammps_gpu, marker='s', label='LAMMPS, GPU')
# ax2.loglog(n, time_ipi_gpu, marker='x', label='i-PI, GPU')
ax2.set_ylabel("Time/Step [s]", size=22)
ax2.set_xlabel("nCPU,nGPU", size=22)
ax2.legend()
# ax2.grid(True, which="both", ls="--")

x = np.arange(1, 500)
ax2.loglog(x, one_n(x, offset=np.exp(1.55)), ls=":", c="grey", lw=2)
ax2.loglog(x, one_n(x, offset=np.exp(3.32)), ls=":", c="grey", lw=2)
ax2.loglog(x, one_n(x, offset=np.exp(5.80)), ls=":", c="grey", lw=2)
ax2.set_ylim(0.3, 410)

x = np.arange(1, 500)
y = np.ones(len(x)) * 10000
ax2.loglog(x, y, ls="-", color="grey", alpha=0.2, label="1 task", lw=4)
ax2.loglog(x, y, ls="-", color="grey", alpha=0.4, label="2 task", lw=4)
ax2.loglog(x, y, ls="-", color="grey", alpha=0.8, label="4 task", lw=4)
ax2.loglog(x, y, ls="-", color="grey", alpha=1, label="8 task", lw=4)
ax2.legend()

ax1.text(0.75, 0.01, "MD", transform=ax1.transAxes, weight="bold")
ax2.text(0.75, 0.01, "PIMD-32", transform=ax2.transAxes, weight="bold")

fig.savefig("deepmd-timing.pdf", dpi=300)

# %%

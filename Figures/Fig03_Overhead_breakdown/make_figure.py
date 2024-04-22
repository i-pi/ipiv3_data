import matplotlib.pyplot as plt
import numpy
import seaborn
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

color_palette = seaborn.color_palette("deep")
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Lucida Grande', 'Verdana']  # example sans-serif fonts
plt.rcParams['font.size'] = 10

def timings_LAMMPS_NVE(N):
    """
    The cost of a LAMMPS simulation for an ideal gas in the NVE ensemble.
    """
    A = 0.0
    B = 1.505028938624661e-08 * 1e3
    return A + B * N

def timings_socket_none_NVE(N, version):
    """
    The cost of an i-PI simulation in the NVE ensemble without any interface.
    """

    if version == '2.6.1':
        A = 0.47
        B = 0.06 * 1e-3
        return A + B * N
    elif version == '3.0':
        A = 0.09
        B = 0.02 * 1e-3
        return A + B * N

def timings_socket_UNIX_NVE(N, version):
    """
    The cost of an i-PI simulation in the NVE ensemble with an ideal gas UNIX socket.
    """

    if version == '2.6.1':
        A = 1.03
        B = 0.17 * 1e-3
        return A + B * N
    elif version == '3.0':
        A = 0.34
        B = 0.08 * 1e-3
        return A + B * N

def timings_socket_none_NVTsvr(N, version):
    """
    The cost of an i-PI simulation in the NVT ensemble (svr thermostat) without any interface.
    """

    if version == '2.6.1':
        A = 0.56
        B = 0.07 * 1e-3
        return A + B * N
    elif version == '3.0':
        A = 0.14
        B = 0.03 * 1e-3
        return A + B * N


def ipi_overhead_python(N, version):
    """
    """

    return timings_socket_none_NVE(N, version) - timings_LAMMPS_NVE(N)


def ipi_overhead_communication(N, version):
    """
    """

    return timings_socket_UNIX_NVE(N, version) - timings_socket_none_NVE(N, version)

def ipi_overhead(N, version):
    """
    """

    return timings_socket_UNIX_NVE(N, version) - timings_LAMMPS_NVE(N)


fig, axs = plt.subplots(1, 3, sharey=True, sharex = True, figsize=(3.65 * 2, 3.65 * 0.80))

system_size = [8, 1024, 8192, 65536]

system_size_interpolation = numpy.linspace(1, 10**6, 1000)

code_version = ['3.0', '2.6.1']

# plot in each panel the total, python and communication overheads. Include both versions of the code in each panel.
axs[0].plot(system_size_interpolation, [timings_LAMMPS_NVE(int(N)) for N in system_size_interpolation], color='black', linestyle='--',label='LAMMPS')

for version_index, version in enumerate(code_version):

    # plot the total overhead
    axs[0].set_title('Timing NVE', fontsize=10)
    axs[0].scatter(system_size, [timings_socket_UNIX_NVE(int(N), version) for N in system_size], label='v' + version, color=color_palette[version_index], marker='o')
    axs[0].plot(system_size_interpolation, [timings_socket_UNIX_NVE(int(N), version) for N in system_size_interpolation], color=color_palette[version_index], linestyle='--')

    # plot the total overhead
    axs[1].set_title('Python overhead', fontsize=10)
    axs[1].scatter(system_size, [ipi_overhead_python(int(N), version) for N in system_size], label='v' + version, color=color_palette[version_index], marker='o')
    axs[1].plot(system_size_interpolation, [ipi_overhead_python(int(N), version) for N in system_size_interpolation], color=color_palette[version_index], linestyle='--')

    # plot the python overhead
    axs[2].set_title('Communication overhead', fontsize=10)
    axs[2].scatter(system_size, [ipi_overhead_communication(int(N), version) for N in system_size], color=color_palette[version_index], marker='o')
    axs[2].plot(system_size_interpolation, [ipi_overhead_communication(int(N), version) for N in system_size_interpolation], color=color_palette[version_index], linestyle='--')

axs[1].set_xscale('log')
axs[1].set_yscale('log')


for i in range(3):
    axs[i].set_xlabel('Number of atoms')
    axs[i].grid(ls='--', lw=0.5)



axs[0].set_ylabel('time per step [ms/step]')
axs[0].legend(loc='upper left')

# add panels "a", "b", "c" to top left of every pabel in bold font

for ax, label in zip(axs, ['a', 'b', 'c']):
    ax.text(-0.05, 1.05, label, transform=ax.transAxes, fontsize=10, fontweight='bold', va='top', ha='right')


axs[0].set_ylim(0.06,90)

plt.tight_layout()
plt.savefig('overhead_breakdown.pdf', dpi=300)



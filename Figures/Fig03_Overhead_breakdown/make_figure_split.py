import matplotlib.pyplot as plt
import numpy
import seaborn
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

color_palette = seaborn.color_palette("deep")
#plt.rcParams['font.family'] = 'sans-serif'
#plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Lucida Grande', 'Verdana']  # example sans-serif fonts
#plt.rcParams['font.size'] = 10

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



for iplot in range(3):
    fig, axs = plt.subplots(1)#,figsize=(3.65,3.65*0.80))# , 3, sharey=True, sharex = True, figsize=(3.65 * 2, 3.65 * 0.80))
    system_size = [8, 1024, 8192, 65536]
    system_size_interpolation = numpy.linspace(1, 10**6, 1000)
    code_version = ['3.0', '2.6.1']

    # plot in each panel the total, python and communication overheads. Include both versions of the code in each panel.

    for version_index, version in enumerate(code_version):

        if iplot == 0:
            # plot the total overhead
            axs.set_title('Timing NVE', fontsize=10)
            axs.scatter(system_size, [timings_socket_UNIX_NVE(int(N), version) for N in system_size], label='v' + version, color=color_palette[version_index], marker='o')
            axs.plot(system_size_interpolation, [timings_socket_UNIX_NVE(int(N), version) for N in system_size_interpolation], color=color_palette[version_index], linestyle='--')
            axs.plot(system_size_interpolation, [timings_LAMMPS_NVE(int(N)) for N in system_size_interpolation], color='black', linestyle='--',label='LAMMPS')
            output_filename = 'timing_NVE.pdf'
        elif iplot == 1:
            # plot the total overhead
            axs.set_title('Python overhead', fontsize=10)
            axs.scatter(system_size, [ipi_overhead_python(int(N), version) for N in system_size], label='v' + version, color=color_palette[version_index], marker='o')
            axs.plot(system_size_interpolation, [ipi_overhead_python(int(N), version) for N in system_size_interpolation], color=color_palette[version_index], linestyle='--')
            output_filename = 'overhead_python.pdf'
        elif iplot == 2:
            # plot the python overhead
            axs.set_title('Communication overhead', fontsize=10)
            axs.scatter(system_size, [ipi_overhead_communication(int(N), version) for N in system_size], color=color_palette[version_index], marker='o')
            axs.plot(system_size_interpolation, [ipi_overhead_communication(int(N), version) for N in system_size_interpolation], color=color_palette[version_index], linestyle='--')
            output_filename = 'overhead_communication.pdf'

    axs.set_aspect(1.6)
    axs.set_xscale('log')
    axs.set_yscale('log')

    axs.set_xlabel('Number of atoms')
    axs.grid(ls='--', lw=0.5)
    axs.set_ylim(0.06,90)

    if iplot == 0:
        axs.set_ylabel('time per step (ms/step)')
        axs.legend(loc='upper left')

    plt.tight_layout()
    plt.savefig(output_filename, dpi=300)



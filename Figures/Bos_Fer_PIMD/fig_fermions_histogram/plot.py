import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Define axes
x_label=r"$\langle E \rangle / \hbar \omega_0$"
y_label="P(E)"


# Define format
plt.rc("font", **{"family": "sans-serif", "sans-serif": ["Arial"]})
tick_major_size = 10
tick_minor_size = 7
labelsize = 20
fontsize = 18
legend_fontsize = 15

plt.rcParams["font.size"] = fontsize
plt.rc("axes", linewidth=2, labelpad=10)
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"
plt.rc("xtick.major", size=tick_major_size, width=2)
plt.rc("xtick.minor", size=tick_minor_size, width=2)
plt.rc("ytick.major", size=tick_major_size, width=2)
plt.rc("ytick.minor", size=tick_minor_size, width=2)


def plot(x_label, y_label, temp_kelvin):

    #Load data
    bin_edges = np.loadtxt("data/%s_bosonic_hist_edges.txt" % str(temp_kelvin))
    density = np.loadtxt("data/%s_bosonic_hist_density.txt" % str(temp_kelvin))
    plt.plot(bin_edges[:-1], density, "o", label="bosonic energy")
    bin_edges = np.loadtxt("data/%s_fermionic_hist_edges.txt" % str(temp_kelvin))
    density = np.loadtxt("data/%s_fermionic_hist_density.txt" % str(temp_kelvin))


    #Plot
    plt.plot(bin_edges[:-1], density, "o", label="fermionic energy")

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend(loc="upper left", fontsize=legend_fontsize)

    plt.savefig(
        "ipi_noninteracting-fermions_energy_hist_3_%s.pdf" % str(temp_kelvin),
        bbox_inches="tight",
    )
    plt.show()


if __name__ == "__main__":
    plot(x_label, y_label, temp_kelvin=23.22)
    plot(x_label, y_label, temp_kelvin=46.46)

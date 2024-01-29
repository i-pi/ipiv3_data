import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#Define axes
x_label=r'$\beta \hbar \omega_0$'
y_label=r'$\langle E \rangle / (N \hbar \omega_0)$'

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

def plot(x_label, y_label):
       num_bosons = 512

       # results
       for ptype in ['distinguishable', 'bosons']:
           x = np.loadtxt('data/%s_%s_x' % (num_bosons, ptype))
           y = np.loadtxt('data/%s_%s_y' % (num_bosons, ptype))
           err = np.loadtxt('data/%s_%s_err' % (num_bosons, ptype))
           plt.errorbar(x, y / num_bosons, err / num_bosons, linestyle='None', marker='o', label='%s' % ptype)

       # analytical baseline
       for is_distinguishable in [True, False]:
           q = np.linspace(x[0]-0.1, x[-1]+0.1, 100)
           vectorized_analytical_func = np.vectorize(lambda t: analytical_energy_bhw(num_bosons, t, is_distinguishable, dim=3) / num_bosons)
           p = vectorized_analytical_func(q)
           plt.plot(q, p, linestyle='--', color='black')
           plt.fill_between(q, p - 0.005 * p, p + 0.005 * p,alpha=0.3, facecolor='grey')

       plt.gca().set_ylim(763.0 / num_bosons, 800.0 / num_bosons)

       plt.legend(loc="center left", fontsize=legend_fontsize)

       plt.xlabel(x_label)
       plt.ylabel(y_label)
       # plt.gca().yaxis.set_label_coords(-.15, 1)

       plt.savefig('ipi_noninteracting_temperature_512.pdf', bbox_inches='tight')
       plt.show()

def zk(bhw, k, d):
    return pow(1 / (1 - np.exp(-k * bhw)), d)

def dzk(bhw, k, d):
    return -0.5 * k * d * zk(bhw, k, d) * \
                (1 + np.exp(- k * bhw)) / (1 - np.exp(- k * bhw))

def boson_energy(bhw, N, d):
    zs = np.zeros(N + 1)
    dzs = np.zeros(N + 1)
    zs[0] = 1
    dzs[0] = 0
    for m in range(1, N + 1):
        sig_z = 0.0
        sig_dz = 0.0
        for k in range(1, m + 1):
            sig_dz += (1 / m) * (dzk(bhw, k, d) * zs[m - k] + zk(bhw, k, d) * dzs[m - k])
            sig_z += (1 / m) * (zk(bhw, k, d) * zs[m - k])
        zs[m] = sig_z
        dzs[m] = sig_dz
    return (-1 / zs[N] * dzs[N])

def distinguishable_energy(bhw, N, d):
    return boson_energy(bhw, 1, d) * N

def analytical_energy_bhw(num_bosons, bhw, is_distinguishable, dim=3, is_fermions=False):
    N = num_bosons

    if is_fermions:
         return fermion_energy(bhw, N, dim)
    if not is_distinguishable:
         return boson_energy(bhw, N, dim)
    return distinguishable_energy(bhw, N, dim)

def analytical_energy(num_bosons, temperature_kelvin, is_distinguishable, dim=3):
    """Credit: Nentanel Bachar-Schwartz, Jacob Higer"""
    spring_constant = 1.21647924E-8
    mass = 1.0
    omega = np.sqrt(spring_constant / mass)

    # Boltzmann = scipy.constants.Boltzmann
    Boltzmann = 1
    # hbar = scipy.constants.hbar
    hbar = 1

    temperature = temperature_kelvin * 3.1668152e-06 # see units.py of i-pi for conversion to atomic units

    beta = (1 / (Boltzmann * temperature))

    bhw = beta * hbar * omega

    return analytical_energy_bhw(num_bosons, bhw, is_distinguishable, dim=dim, is_fermions=is_fermions) * hbar * omega


if __name__ == '__main__':
    plot(x_label,y_label)

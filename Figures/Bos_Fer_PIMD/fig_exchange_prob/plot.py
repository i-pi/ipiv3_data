import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#Define axes
x_label = r'$\beta \hbar \omega_0$'
y_label = r'exchange-all $/$ $(1/N)$'


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

   #Load data
   label = 'longest'
   x = np.loadtxt('data/%s_x' % label)
   y = np.loadtxt('data/%s_y' % label)
   err = np.loadtxt('data/%s_err' % label)


   #Plot
   plt.errorbar(x, y, err, linestyle='None', marker='o')#, label=label)

   plt.axhline(1.0, linestyle='--')

   plt.xlabel(x_label)
   plt.ylabel(y_label)
   # plt.legend()

   plt.savefig('bosonic_gauge_16_3_beads_5000000.pdf', bbox_inches='tight')
   plt.show()

if __name__ == '__main__':

    plot(x_label,y_label)

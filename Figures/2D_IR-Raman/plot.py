import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os
import matplotlib as mpl
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator, FormatStrFormatter)
from mpl_toolkits.axes_grid1 import ImageGrid
import matplotlib.patches as mpatches

#Define axes
x_label = r'$\omega_1 / 2 \pi c\ [{\rm cm}^{-1}]$'
y_label_left =  r'$\omega_2 / 2 \pi c\ [{\rm cm}^{-1}]$'
y_label_right = r'$R(\omega_1, \omega_2)$' # [10^6 \ \rm au]$'

# Define format
plt.rc("font", **{"family": "sans-serif", "sans-serif": ["Arial"]})
tick_major_size = 10
tick_minor_size = 7
labelsize = 20
fontsize = 18
legend_fontsize = 15
figsize=(6,3)

plt.rcParams["font.size"] = fontsize
plt.rc("axes", linewidth=2, labelpad=10)
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"
plt.rc("xtick.major", size=tick_major_size, width=2)
plt.rc("xtick.minor", size=tick_minor_size, width=2)
plt.rc("ytick.major", size=tick_major_size, width=2)
plt.rc("ytick.minor", size=tick_minor_size, width=2)


#Define constants
fstoau = 41.34137 # Femtosecond to a.u.
autocm1 = 219474.63 # a.u. (Hartree energy unit) to wavenumber
invfstocm1 = autocm1/fstoau #fs^-1 to cm^-1 conversion

def plot(x_label, y_label,mode):

    #Load data
    specMD = np.loadtxt('MD.txt')
    specTRPMD = np.loadtxt('TRPMD.txt')

    #Define variables
    dt = 1 * fstoau #Timestep
    nplot = 350
    dw = 2*np.pi / 2501 / dt * autocm1 #Frequency step for fft
    wmin=0 #Minimin frequency
    wmax=nplot*dw #Maximum frequency

    #Plot settings:
    #plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica'], 'size': 8})
    #plt.rc('text', usetex=True)
    #plt.rc('text.latex', preamble=r'\usepackage[helvet]{sfmath}')


    #cbarticks1 = [-0.3, -0.15, 0.0, 0.15, 0.3]
    #cbarticklabels1 = ['-0.30', '-0.15', '0.00', '0.15', '0.30']
    #cbarticks2 = [-0.15, -0.10, -0.05, 0.0, 0.05, 0.10, 0.15]
    #cbarticklabels2 = ['-0.15', '-0.10', '-0.05', '0.00', '0.05', '0.10', '0.15']
    cbarticks1 = [-1.00, -0.50, 0.0, 0.50, 1.00]
    cbarticklabels1 = ['-1.00', '-0.50', '0.00', '0.50', '1.00']
    cbarticks2 = [-1.00, -0.50, 0.0, 0.50, 1.00]
    cbarticklabels2 = ['-1.00', '-0.50', '0.00', '0.50', '1.00']

    fig, axs = plt.subplots(1, 2, figsize=(6.6, 3.0),  gridspec_kw={'width_ratios': [0.445, 0.555]})

    for j in range(1):
            vmin=-0.31
            vmax=0.31
            vmin=-1.1
            vmax=1.1
            levels = np.arange(vmin, vmax,0.2)
            norm_factor = 1/0.3
            for i in range(2):
                spec = [specMD, specTRPMD][i]
                ax = axs[i]
                cs = ax.contourf(spec * norm_factor,levels=levels, vmin=vmin, vmax=vmax,cmap=mpl.cm.bwr, extend='both', extent=(wmin,wmax,wmin,wmax))
                cs2 = ax.contour(spec * norm_factor,levels=levels, vmin=vmin, vmax=vmax,colors='tab:grey', alpha=0.4, extent=(wmin,wmax,wmin,wmax))
                ax.set_xlim([-50, 1200])
                ax.set_ylim([2900, 4100])
                ax.set_aspect('equal', adjustable='box')
                ax.set_title([r'Classical MD', r'TRPMD'][i], x = 0.45, y = 0.99, fontsize = fontsize)
                ax.xaxis.set_ticks_position('both')
                ax.yaxis.set_ticks_position('both')
                ax.tick_params(which='both', direction='in', labelleft = [True, False][i])
                ax.xaxis.set_major_locator(MultipleLocator(500))
                ax.xaxis.set_minor_locator(MultipleLocator(100))
                ax.yaxis.set_major_locator(MultipleLocator(500))
                ax.yaxis.set_minor_locator(MultipleLocator(250))
            cbar = fig.colorbar(cs, ax=ax, shrink = 0.8, location = 'right', aspect = 15, extendrect=True)
            #cbar.add_lines(cs2)
            cbar.ax.set_ylabel(y_label_right, labelpad = 27.5, rotation=270)
            cbar.set_ticks([cbarticks1, cbarticks2][j])
            cbar.set_ticklabels([cbarticklabels1, cbarticklabels2][j])
            for t in cbar.ax.get_yticklabels():
             t.set_horizontalalignment('right')
             t.set_x(4.5)

            plt.subplots_adjust(left=0.17,
                        bottom=0.03,
                        right=0.87,
                        top=1.02,
                        wspace=0.05,
                        hspace=-0.2)

            fig.text(0.02, 0.53, y_label_left, va='center', rotation='vertical')
            fig.text(0.5, 0.015, x_label, ha='center')

            plt.savefig('2D_IR_Raman_spectra.pdf')

if __name__ == '__main__':
    plot(x_label,y_label_left,y_label_right)

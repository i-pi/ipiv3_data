import numpy
import matplotlib.pyplot as plt
import seaborn as sns

blue_color = sns.color_palette("deep")[0]
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
figsize1=(6,4)
figsize2=(6,3)

#f, ax =plt.subplots(1,3, figsize=(3.8 * 2, 3.8), sharex=True)

for iplot in range(3):
    if iplot == 0:
        f, ax =plt.subplots(1, figsize=figsize1)
        ax.set_xlabel(r'$\omega$ (cm$^{-1}$)')
        ax.set_xlim(0, 4200)
        ax.set_ylabel(r'Intensity (a.u.)')
        ax.set_ylim(-.3, 4)
        ax.set_title('IR')
        gr = numpy.loadtxt('../water/production-small/md-liquid/mm_der_facf.data')
        ax.plot(gr.T[0]* 219474, gr.T[1] * 200 + 2, color=blue_color, label='MD', ls='--')
        
        gr = numpy.loadtxt('../water/production-small/tepigs-liquid/mm_der_facf.data')
        ax.plot(gr.T[0] * 219474, gr.T[1] * 200 + 1,color=blue_color, label='Te PIGS')
        
        gr = numpy.loadtxt('../experimental-data/water_300K_IR.data', usecols=(0,1))
        ax.plot(gr.T[0], gr.T[1], color='k', label='experiment')
        ax.legend(ncol=3)
        plt.savefig('tepigs_example_1.pdf', bbox_inches='tight')

    elif iplot == 1:
        f, ax =plt.subplots(1, figsize=figsize2)
        ax.set_xlabel(r'$\omega$ (cm$^{-1}$)')
        ax.set_xlim(0, 4200)
        ax.set_ylabel(r'Intensity (a.u.)')
        ax.set_title('Isotropic Raman')
        gr = numpy.loadtxt('../experimental-data/water_300K_Raman_high_frequency_iso.csv', usecols=(0,1))
        ax.plot(gr.T[0], gr.T[1] / numpy.max(gr.T[1]), color='k', label='experiment')
        
        gr = numpy.loadtxt('../experimental-data/water_300K_Raman_low_frequency_iso.csv', usecols=(0,1))
        ax.plot(gr.T[0], gr.T[1] / numpy.max(gr.T[1]), color='k', label='experiment')
        
        gr = numpy.loadtxt('../water/production-small/tepigs-liquid/L0_der_facf.data', usecols=(0,1))
        w, f = (gr[gr.T[0] * 219474 > 2800]).T
        ax.plot(w * 219474, f / numpy.max(f) + 1, color=blue_color, label='Te PIGS')
        
        gr = numpy.loadtxt('../water/production-small/tepigs-liquid/L0_der_facf.data', usecols=(0,1))
        w, f = (gr[gr.T[0] * 219474 < 2400]).T
        ax.plot(w * 219474, f / numpy.max(f) + 1, color=blue_color, label='Te PIGS')
        
        gr = numpy.loadtxt('../water/production-small/md-liquid/L0_der_facf.data', usecols=(0,1))
        w, f = (gr[gr.T[0] * 219474 > 2800]).T
        ax.plot(w * 219474, f / numpy.max(f) + 2, color=blue_color, label='MD', ls='--')
        
        gr = numpy.loadtxt('../water/production-small/md-liquid/L0_der_facf.data', usecols=(0,1))
        w, f = (gr[gr.T[0] * 219474 < 2400]).T
        ax.plot(w * 219474, f / numpy.max(f) + 2, color=blue_color, label='MD', ls='--')
        plt.savefig('tepigs_example_2.pdf', bbox_inches='tight')

    elif iplot == 2:
        f, ax =plt.subplots(1, figsize=figsize2)
        ax.set_xlabel(r'$\omega$ (cm$^{-1}$)')
        ax.set_xlim(0, 4200)
        ax.set_ylabel(r'Intensity (a.u.)')
        ax.set_title('Anisotropic Raman')
        gr = numpy.loadtxt('../experimental-data/water_300K_Raman_high_frequency.csv', usecols=(0,1))
        ax.plot(gr.T[0], gr.T[1], color='k', label='experiment')
        
        gr = numpy.loadtxt('../experimental-data/water_300K_Raman_low_frequency.csv', usecols=(0,1))
        ax.plot(gr.T[0], gr.T[1], color='k', label='experiment')
        
        
        gr = numpy.loadtxt('../water/production-small/tepigs-liquid/L2_der_facf.data', usecols=(0,1))
        w, f = (gr[gr.T[0] * 219474 > 2800]).T
        ax.plot(w * 219474, f / numpy.max(f) + 1, color=blue_color, label='Te PIGS')
        
        gr = numpy.loadtxt('../water/production-small/tepigs-liquid/L2_der_facf.data', usecols=(0,1))
        w, f = (gr[gr.T[0] * 219474 < 2400]).T
        ax.plot(w * 219474, f / numpy.max(f) + 1, color=blue_color, label='Te PIGS')
       
        gr = numpy.loadtxt('../water/production-small/md-liquid/L2_der_facf.data', usecols=(0,1))
        w, f = (gr[gr.T[0] * 219474 > 2800]).T
        ax.plot(w * 219474, f / numpy.max(f) + 2, color=blue_color, label='MD', ls='--')
        
        gr = numpy.loadtxt('../water/production-small/md-liquid/L2_der_facf.data', usecols=(0,1))
        w, f = (gr[gr.T[0] * 219474 < 2400]).T
        ax.plot(w * 219474, f / numpy.max(f) + 2, color=blue_color, label='MD', ls='--')
        plt.savefig('tepigs_example_3.pdf', bbox_inches='tight')


#for iax in ax:
#    iax.grid()
#    if iax == ax[1]:    iax.set_ylabel(r'IR Intensity [arb.]')
#    iax.set_yticklabels([])



import numpy
import matplotlib.pyplot as plt
import seaborn as sns

blue_color = sns.color_palette("deep")[0]

f, ax =plt.subplots(1,3, figsize=(3.8 * 2, 3.8), sharex=True)

ax[0].set_title('Ambient condition liquid water vibrational spectrum')


ax[0].set_title('IR')
ax[1].set_title('Isotropic Raman')
ax[2].set_title('Anisotropic Raman')

ax[-1].set_xlabel(r'$\omega$ [cm$^{-1}$]')
ax[0].set_xlim(0, 4500)

gr = numpy.loadtxt('../water/production-small/md-liquid/mm_der_facf.data')
ax[0].plot(gr.T[0]* 219474, gr.T[1] * 200 + 2, color=blue_color, label='MD', ls='--')

gr = numpy.loadtxt('../water/production-small/tepigs-liquid/mm_der_facf.data')
ax[0].plot(gr.T[0] * 219474, gr.T[1] * 200 + 1,color=blue_color, label='Te PIGS')

gr = numpy.loadtxt('../experimental-data/water_300K_IR.data', usecols=(0,1))
ax[0].plot(gr.T[0], gr.T[1], color='k', label='experiment')





gr = numpy.loadtxt('../experimental-data/water_300K_Raman_high_frequency_iso.csv', usecols=(0,1))
ax[1].plot(gr.T[0], gr.T[1] / numpy.max(gr.T[1]), color='k', label='experiment')

gr = numpy.loadtxt('../experimental-data/water_300K_Raman_low_frequency_iso.csv', usecols=(0,1))
ax[1].plot(gr.T[0], gr.T[1] / numpy.max(gr.T[1]), color='k', label='experiment')

gr = numpy.loadtxt('../water/production-small/tepigs-liquid/L0_der_facf.data', usecols=(0,1))
w, f = (gr[gr.T[0] * 219474 > 2800]).T
ax[1].plot(w * 219474, f / numpy.max(f) + 1, color=blue_color, label='Te PIGS')

gr = numpy.loadtxt('../water/production-small/tepigs-liquid/L0_der_facf.data', usecols=(0,1))
w, f = (gr[gr.T[0] * 219474 < 2400]).T
ax[1].plot(w * 219474, f / numpy.max(f) + 1, color=blue_color, label='Te PIGS')

gr = numpy.loadtxt('../water/production-small/md-liquid/L0_der_facf.data', usecols=(0,1))
w, f = (gr[gr.T[0] * 219474 > 2800]).T
ax[1].plot(w * 219474, f / numpy.max(f) + 2, color=blue_color, label='MD', ls='--')

gr = numpy.loadtxt('../water/production-small/md-liquid/L0_der_facf.data', usecols=(0,1))
w, f = (gr[gr.T[0] * 219474 < 2400]).T
ax[1].plot(w * 219474, f / numpy.max(f) + 2, color=blue_color, label='MD', ls='--')


gr = numpy.loadtxt('../experimental-data/water_300K_Raman_high_frequency.csv', usecols=(0,1))
ax[2].plot(gr.T[0], gr.T[1], color='k', label='experiment')

gr = numpy.loadtxt('../experimental-data/water_300K_Raman_low_frequency.csv', usecols=(0,1))
ax[2].plot(gr.T[0], gr.T[1], color='k', label='experiment')


gr = numpy.loadtxt('../water/production-small/tepigs-liquid/L2_der_facf.data', usecols=(0,1))
w, f = (gr[gr.T[0] * 219474 > 2800]).T
ax[2].plot(w * 219474, f / numpy.max(f) + 1, color=blue_color, label='Te PIGS')

gr = numpy.loadtxt('../water/production-small/tepigs-liquid/L2_der_facf.data', usecols=(0,1))
w, f = (gr[gr.T[0] * 219474 < 2400]).T
ax[2].plot(w * 219474, f / numpy.max(f) + 1, color=blue_color, label='Te PIGS')

gr = numpy.loadtxt('../water/production-small/md-liquid/L2_der_facf.data', usecols=(0,1))
w, f = (gr[gr.T[0] * 219474 > 2800]).T
ax[2].plot(w * 219474, f / numpy.max(f) + 2, color=blue_color, label='MD', ls='--')

gr = numpy.loadtxt('../water/production-small/md-liquid/L2_der_facf.data', usecols=(0,1))
w, f = (gr[gr.T[0] * 219474 < 2400]).T
ax[2].plot(w * 219474, f / numpy.max(f) + 2, color=blue_color, label='MD', ls='--')






ax[0].legend(loc='upper left', frameon=False)

#for iax in ax:
#    iax.grid()
#    if iax == ax[1]:    iax.set_ylabel(r'IR Intensity [arb.]')
#    iax.set_yticklabels([])

plt.savefig('tepigs_example.pdf', bbox_inches='tight')


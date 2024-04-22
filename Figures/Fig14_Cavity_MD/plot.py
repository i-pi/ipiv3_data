import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#Define axes
x_label = r'Frequency (cm$^{-1}$)'
y_label = r'$\eta(\omega)\alpha(\omega)$ (arb. units)'
y_label = r'$I_\text{IR}$ (arb. units)'


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

def plot(x_label, y_label,mode):

   #Load data
   x1,y1,x2,y2,x3,y3 = np.loadtxt('data_plt.txt',unpack=True)

   if mode == 1:
     x=x1
     y=y1
     colour='black'
     output_name='outside_cavity.pdf'
     y_max = 1.0
     polariton=False
   elif mode == 2:
     x=x2
     y=y2
     colour='green'
     output_name='in_cavity_weak.pdf'
     y_max = 1.8
     polariton=True
     freq_LP = 3400
     int_LP = 1.0
     freq_UP = 3850
     int_UP = 1.5
   elif mode == 3:
     x=x3
     y=y3
     colour='blue'
     output_name='in_cavity_strong.pdf'
     y_max = 5.5
     polariton=True
     freq_LP = 3300
     int_LP = 1.0
     freq_UP = 4050
     int_UP = 3.5

   #Plot
   fig, ax = plt.subplots(figsize=figsize)
   ax.plot(x,y,color=colour)
   ax.set_xlim([3000,4250])
   ax.set_ylim([-0.1,y_max])
   ax.set_xlabel(x_label, fontsize=labelsize)
   ax.set_ylabel(y_label, fontsize=labelsize)
   plt.locator_params(axis='x', nbins=5)

   if polariton:
       plt.annotate('LP',(freq_LP, int_LP), fontsize = fontsize)
       plt.annotate('UP',(freq_UP, int_UP), fontsize = fontsize)

   # plt.legend()
   plt.savefig(output_name,bbox_inches='tight')
   #plt.show()

if __name__ == '__main__':
    for mode in [1,2,3]:
     plot(x_label,y_label,mode)

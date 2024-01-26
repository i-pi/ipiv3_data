import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
#from toolkit.tools import  convert as c

#Define axes
#See bottom of this file

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

# Define constants
#eV2au = c.eV2au
eV2au = 0.036749326
units='eV'

def plot(x1_label,x2_label, y_label,input_files,output_filename):

   pes_name=input_files[0]
   inst_name=input_files[1]

   #Load data
   pos,pot,friction = np.loadtxt(pes_name,unpack=True)
   #pot = pot - np.min(pot)
   inst_pos, inst_pot = np.loadtxt(inst_name,unpack=True )
   if units=='eV':
      pot /=eV2au
   elif units=='Ha':
      inst_pot *=eV2au
   else:
     raise NotImplementedError

   min_pot = np.min(pot)
   if True:
      inst_pot -=min_pot
      pot -=min_pot
   fig, ax = plt.subplots()

   #Plot data
   ax.plot(pos, pot, color="black")
   ax.plot(inst_pos, inst_pot, color="red", marker="o")
   #ax.set_xlabel("Mass scaled pathway ($\mathrm{\AA}$ amu$^{0.5}$)", fontsize=labelsize)
   ax.set_xlabel(x1_label, fontsize=labelsize)
   ax.set_ylabel(y_label, color="red", fontsize=labelsize)
   ax.set_xlim([-1.50,1.50])
   ax.set_ylim([-0.01,0.35])
   #plt.xticks(fontsize=ticksize)
   #plt.yticks(fontsize=ticksize)
   plt.locator_params(axis='y', nbins=6)
   plt.locator_params(axis='x', nbins=5)


   # twin object for two different y-axis on the sample plot
   # make a plot with different y-axis using second axis object
   ax2 = ax.twinx()
   ax2.plot(pos, friction, color="blue",linestyle='--')
   ax2.set_ylabel(x2_label, color="blue", fontsize=labelsize)

   #plt.xticks(fontsize=ticksize)
   ax2.set_ylim([-1.0,30])
   #plt.yticks(fontsize=ticksize)
   plt.locator_params(axis='y', nbins=5)

   # save the plot as a file
   plt.savefig(output_filename,bbox_inches='tight')
   print('please check {}'.format(output_filename))

if __name__ == '__main__':

   x1_label= "Mass scaled pathway (a.u.)"
   x2_label=r'$\tilde{\eta}$ (a. u.)'
   y_label="Potential Energy (a.u.)"

   output_filename ='instanton.pdf'
   pes_name='pes1.dat'
   inst_name='inst1.dat'
   plot(x1_label,x2_label, y_label,[pes_name,inst_name],output_filename)

   output_filename ='instanton_constantFriction.pdf'
   pes_name='pes2.dat'
   inst_name='inst2.dat'
   plot(x1_label,x2_label, y_label,[pes_name,inst_name],output_filename)

   output_filename ='instanton_SDFriction.pdf'
   pes_name='pes3.dat'
   inst_name='inst3.dat'
   plot(x1_label,x2_label, y_label,[pes_name,inst_name],output_filename)


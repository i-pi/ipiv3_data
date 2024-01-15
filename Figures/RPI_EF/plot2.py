import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from toolkit.tools import  convert as c
eV2au = c.eV2au
pes_name='pes2.dat'
inst_name='inst2.dat'
units='eV'
rc("font", **{"family": "sans-serif", "sans-serif": ["Arial"]})
ticksize=18
labelsize=20
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
ax.plot(pos, pot, color="black")
ax.plot(inst_pos, inst_pot, color="red", marker="o")
#ax.set_xlabel("Mass scaled pathway ($\mathrm{\AA}$ amu$^{0.5}$)", fontsize=labelsize)
ax.set_xlabel("Mass scaled pathway (a.u.) ", fontsize=labelsize)
ax.set_ylabel("Potential Energy (a.u.)".format(units), color="red", fontsize=labelsize)
ax.set_xlim([-1.50,1.50])
ax.set_ylim([-0.01,0.35])
plt.xticks(fontsize=ticksize)
plt.yticks(fontsize=ticksize)
plt.locator_params(axis='y', nbins=6)
plt.locator_params(axis='x', nbins=5)


# twin object for two different y-axis on the sample plot
# make a plot with different y-axis using second axis object
ax2 = ax.twinx()
ax2.plot(pos, friction, color="blue",linestyle='--')
ax2.set_ylabel(r'$\tilde{\eta}$ (a. u.)', color="blue", fontsize=labelsize)

plt.xticks(fontsize=ticksize)
ax2.set_ylim([-1.0,30])
plt.yticks(fontsize=ticksize)
plt.locator_params(axis='y', nbins=5)


# save the plot as a file
plt.savefig('instanton_constantFriction.pdf',bbox_inches='tight')

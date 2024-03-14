import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from ase.io import read
import os
from matplotlib.lines import Line2D
from function import *
if not os.path.exists("images"):
    os.mkdir("images")


fontsize = 20

################################
# DATA
Emodes = pd.read_csv("energy.csv",header=None)
au2eV = 27.211383414215543 # convert(1,"energy","atomic_unit","electronvolt")
Emodes *= au2eV
trajectory = read("trajectory.extxyz",index=":")
time =  np.asarray([ a.info["time"] for a in trajectory ]) * 0.0241888434619721 # convert(1,"time","atomic_unit","femtosecond")

Etot = np.asarray([ a.info["conserved"] for a in trajectory ])
Etot -= trajectory[0].info["potential"]
Etot *= au2eV

################################
# PLOT
fig,ax = plt.subplots(figsize=(10,5))

# Set font sizes
plt.rcParams.update({'font.size': fontsize})  # Increase font size for all text
# Set tick sizes
ax.tick_params(axis='both', which='major', labelsize=fontsize, width=1.5, length=6)  # Increase major tick size
ax.tick_params(axis='both', which='minor', width=1.5, length=4)  # Increase minor tick size


# Normal modes energy
argv = {
    "linestyle":"solid",
    "linewidth":2,
    "alpha":1.0
}
ax.plot(time,Emodes[6],label=r'E$_{\rm bend}$',c="firebrick",zorder=0,**argv)
ax.plot(time,Emodes[7],label=r'E$_{\rm str,sym}$',c="blue",zorder=0,**argv)
ax.plot(time,Emodes[8],label=r'E$_{\rm str,asym}$',c="orange",zorder=0,**argv)

# Total energy and anharmonic contribution
argv = {
    "linestyle":"solid", 
    "linewidth":2,
    "alpha":1
}
Eharm = Emodes.sum(axis=1)
Eanharm = Etot - Eharm
ax.plot(time,Etot,c="black",label=r'E$_{\rm tot}$',**argv)
ax.plot(time,Eanharm,c="olivedrab",label=r'E$_{\rm anharm}$',**argv)

# Efield
ax2 = ax.twinx()
au2eVa = 51.42206747645111
Efield = au2eVa * np.asarray([ a.info["Efield"] for a in trajectory ])
A = np.max(Efield)
argv = {
    "linestyle":"solid", 
    "linewidth":1,
    "alpha":0.5
}
ax2.plot(time,Efield[:,1],label=r'$\mathcal{E}$',zorder=0,color="darkorchid",**argv)

remove_empty_space(ax)
argv = {
    "linestyle":"solid",
    "linewidth":0.5,
    "alpha":1
}
hzero(ax2,**argv)
ax2.set_ylim(-3,3)
ax.set_ylim(-0.2,0.7)
ax.set_xlim(0,500)

ax.set_xlabel("time [fs]",fontsize=fontsize)
ax.set_ylabel("energy [eV]",fontsize=fontsize)
ax2.set_ylabel("E-field [eV/ang]",fontsize=fontsize)
ax.grid(linestyle="dashed",alpha=0.7)


legend1 = ax.legend(facecolor='white', ncol=5,
                    framealpha=1, edgecolor="black", loc="lower left", fontsize=fontsize-2, title_fontsize=fontsize-2)

legend2 = ax2.legend(facecolor='white', ncol=2, \
           framealpha=1, edgecolor="black", loc="upper left", fontsize=fontsize-2)

legend1._legend_box.align = "left"
legend2._legend_box.align = "left"

ax.add_artist(legend1)
legend1.set_bbox_to_anchor((-0.15, 1.0))  # Adjust the values as needed

plt.autoscale()
ext="pdf"
plt.savefig(f'images/water.energy.time-series.{ext}',dpi=1200,bbox_inches='tight', bbox_extra_artists=(legend1,))

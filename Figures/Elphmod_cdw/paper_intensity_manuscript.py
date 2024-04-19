#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import elphmod
import numpy as np
import pickle
import sys
import matplotlib.pyplot as plt
plt.style.use('tableau-colorblind10')


"""""""""""""""""""""""""""""""""""""""
Parameters
"""""""""""""""""""""""""""""""""""""""


figx = 7.3
figy = 2.4
capsize = 2
ms = 2
fs = 8.0 
fs_tick = 7.5 # fontsize tick
fs_title = 10 # title
fs_abcd = 10 # fontsize abdc label

#figx = 3.0
#figy = 2.4
figx = 6.0
figy=2.5

linewidth = 1.0 
"""""""""""""""""""""""""""""""""""""""
Arrarys
"""""""""""""""""""""""""""""""""""""""

Std = dict()
Intensity = dict()
T_list = dict()

"""""""""""""""""""""""""""""""""""""""
Load structure factor
"""""""""""""""""""""""""""""""""""""""

intensity_types = ['Total', 'Bragg', 'Diffuse']
panels = ['d', 'b', 'c']

supercell = '18x18'
for int_type in intensity_types:

    T_list['intensity_%s' % supercell], Intensity['CLASSICAL_%s_%s' % (int_type, supercell)], Std['CLASSICAL_block_%s_%s' % (int_type, supercell)] = np.loadtxt(
    'S_TaS2_18x18_N_steps_start=70_N_steps_inter=10_N_steps_end=1056_CLASSICAL/Intensity_%s_%s_CLASSICAL_q-index=6.txt' % (int_type, supercell)).T
    
    T_list['intensity_%s' % supercell], Intensity['PIMD_beads_%s_%s' % (int_type, supercell)], Std['PIMD_beads_block_%s_%s' % (int_type, supercell)] = np.loadtxt(
    'S_TaS2_18x18_N_steps_start=70_N_steps_inter=10_N_steps_end=496_PIMD_beads/Intensity_%s_%s_PIMD_beads_q-index=6.txt' % (int_type, supercell)).T



"""""""""""""""""""""""""""""""""""""""
Plot 1 PANEL
"""""""""""""""""""""""""""""""""""""""

gs_kw = dict(width_ratios=[1], height_ratios=[1])
fig, (ax) = plt.subplots(1,1, figsize=(figx,figy), gridspec_kw=gs_kw)

int_type = 'Total'

for y, ylabel in enumerate([
r'$<S(q=2/3\Gamma M)>$',
]):
    ax.set_ylabel(ylabel, fontsize=fs)
    
for x, xlabel in enumerate([
r'Temperature in K', 
r'Temperature in K',
r'Temperature in K',
]):
    ax.set_xlabel(xlabel, fontsize=fs)

for x in range(1):
    # Set the y-axis limits
    ax.set_ylim(0, 3.5e-4)  # Adjust the values as needed
    ax.set_xlim(50, 200)  # Adjust the values as needed
    # set tick size
    ax.tick_params(axis='both', which='major', labelsize=fs_tick)    


#ax.axvspan(80, 85, facecolor='blue', alpha=0.3)
#ax.axvspan(93, 98, facecolor='cornflowerblue', alpha=0.3)


ax.errorbar(T_list['intensity_%s' % supercell], Intensity['CLASSICAL_%s_%s' % (int_type, supercell)] , Std['CLASSICAL_block_%s_%s' % (int_type, supercell)],
marker = 'o',
color = 'cornflowerblue', 
#    linestyle = 'None',
linestyle = '--',
linewidth = linewidth,
markersize = ms,     
capsize = capsize)

ax.errorbar(T_list['intensity_%s' % supercell], Intensity['PIMD_beads_%s_%s' % (int_type, supercell)] , Std['PIMD_beads_block_%s_%s' % (int_type, supercell)],
marker = 'o',
color = 'blue', 
#    linestyle = 'None',
linestyle = '--',
linewidth = linewidth,
markersize = ms,     
capsize = capsize,
)

# set title
#ax.set_title('%s' % int_type, fontsize=fs_title)
# set panel
ax.text(-0.13, 1.1, '(%s)' % panels[0], transform=ax.transAxes, 
                size=fs_abcd)
   
# y-axis as power             
ax.yaxis.major.formatter.set_powerlimits((0,0))
ax.yaxis.offsetText.set_fontsize(fontsize=fs_tick)




# experimental value?
ax.axvline(x=75, color = 'black', linewidth = linewidth, linestyle = 'dashed')
#    ax[mm].axvline(x=85, color = 'blue',  linewidth = linewidth, linestyle = 'dashed')  
# ax.axvline(x=101.5, color = 'cornflowerblue', linewidth = linewidth, linestyle = 'dashed')  


plt.tight_layout()
# Adjust horizontal spacing between subplots
plt.subplots_adjust(wspace=0.15)  # Adjust the value as needed
plt.savefig('fig_intensity.pdf')
plt.show()





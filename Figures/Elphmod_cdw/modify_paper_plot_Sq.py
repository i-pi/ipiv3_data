#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import elphmod
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('tableau-colorblind10')
from matplotlib import cm
from matplotlib import colors

"""""""""""""""""""""""""""""""""""""""
Parameters
"""""""""""""""""""""""""""""""""""""""

# supercell
N1 = 18
nk = N1
a = 3.386821146*N1

# parameters for the plot
panel = 'e'
fs_panel = 11
figx = 2.2
figy = 2
ms = 16
cb_ticks_font_size = 7

# 4 panels, panel label outside
figx = 1.74
figy = 1.7
ms = 8
fs_panel = 8.5

# 4 panels, panel label inside
figx = 6.0
figy = 1.7
ms = 13
fs_panel = 8.5
b_ticks_font_size = 10

"""""""""""""""""""""""""""""""""""""""
Dictionaries
"""""""""""""""""""""""""""""""""""""""

S = dict()


"""""""""""""""""""""""""""""""""""""""
Lists
"""""""""""""""""""""""""""""""""""""""
T_list = [50, 53.3, 56.8, 60.4, 64.3, 68.3, 72.5, 76.8, 81.3, 86.1, 91.1, 96.5, 102,
          107.8, 113.8, 120.1, 126.8, 133.7,140.9, 148.5, 156.5 , 164.7,173.4,182.5, 192.1, 200.0]
          
#SRT_list = [0,8,11,25]
SRT_list = [0,11,25]


divide = False
class_exponent = 1
quant_exponent = 0
save = 'class'
BZ_color = 'k'
panel_label_list = ['a', 'b', 'c']


#gs_kw = dict(width_ratios=[1, 1, 1, 1.2], height_ratios=[1,1,1])
gs_kw = dict(width_ratios=[1, 1, 1.2], height_ratios=[1])
#fig, (ax) = plt.subplots(3,4, figsize=(figx,figy), gridspec_kw=gs_kw)
fig, (ax) = plt.subplots(1,3, figsize=(figx,figy), gridspec_kw=gs_kw)

"""""""""""""""""""""""""""""""""""""""
FIRST ROW!
"""""""""""""""""""""""""""""""""""""""
                    
# for ii,(SRT,panel) in enumerate(zip(SRT_list,panel_label_list)):
#
#     print(SRT)
#
#     """""""""""""""""""""""""""""""""""""""
#     Load structure factor
#     """""""""""""""""""""""""""""""""""""""
#
#     S_tmp = np.load('S_TaS2_18x18_N_steps_start=70_N_steps_inter=10_N_steps_end=1056_CLASSICAL/S_%d.npy' % SRT)
#     S['class'] = (S_tmp.sum(axis=0)).reshape(N1*N1) / S_tmp.shape[0]
#
#     S_tmp = np.load('S_TaS2_18x18_N_steps_start=70_N_steps_inter=10_N_steps_end=496_PIMD_beads/S_%d.npy' % SRT)
#     S['quant'] = (S_tmp.sum(axis=0)).reshape(N1*N1) / S_tmp.shape[0]
#
#     S_tmp = np.load('S_TaS2_18x18_N_steps_start=70_N_steps_inter=10_N_steps_end=1056_CLASSICAL/S_%d_BG.npy' % SRT)
#     S['class_BG'] = (S_tmp.sum(axis=0)).reshape(N1*N1) / S_tmp.shape[0]
#
#     S_tmp = np.load('S_TaS2_18x18_N_steps_start=70_N_steps_inter=10_N_steps_end=496_PIMD_beads/S_%d_BG.npy' % SRT)
#     S['quant_BG'] = (S_tmp.sum(axis=0)).reshape(N1*N1) / S_tmp.shape[0]
#
# #    S['class'] = S['class_BG']
# #    S['quant'] = S['quant_BG']
#
#     """""""""""""""""""""""""""""""""""""""
#     Draw Brillouin zone
#     """""""""""""""""""""""""""""""""""""""
#
#     outline = elphmod.bravais.BZ()
#     outline = np.array(outline) / (a / nk)
#     outline = list(outline)
#
#     ax[0,ii].fill_between(*zip(*outline), color = BZ_color)
#     ax[0,ii].plot(*zip(*outline), color='gray',
#     linewidth = 1, alpha=0.4)
#
#     """""""""""""""""""""""""""""""""""""""
#     Choose quantity to plot
#     """""""""""""""""""""""""""""""""""""""
#
#     S_plot = S['class']**(class_exponent) / S['quant']**(quant_exponent)
#
#
#     """""""""""""""""""""""""""""""""""""""
#     Add BZ points from the edge
#     """""""""""""""""""""""""""""""""""""""
#
#     q = np.load('output_kpoints/q_voronoi_%s%s2_%dx%d.npy' % ('Ta','S',N1,N1))
#     q = np.reshape(q,(N1*N1,3))
#     qx = q[:,0] / (2*np.pi)
#     qy = q[:,1] / (2*np.pi)
#
#
#     # K points
#     qx = np.append(qx, np.array([-1.96841415e-01]))
#     qy = np.append(qy, np.array([0]))
#     S_plot = np.append(S_plot, np.array([S_plot[228]]))
#
#     qx = np.append(qx, np.array([1.96841415e-01]))
#     qy = np.append(qy, np.array([0]))
#     S_plot = np.append(S_plot, np.array([S_plot[228]]))
#
#     upper_edge = [228,263,298,9,44,79,114]
#     for shift_index in upper_edge:
#         qx = np.append(qx, np.array([qx[shift_index]]))
#         qy = np.append(qy, np.array([-qy[shift_index]]))
#         S_plot = np.append(S_plot, np.array([S_plot[shift_index]]))
#
#     left_edge = [133,152,171,190,209,79,114,228]
#     for shift_index in left_edge:
#         qx = np.append(qx, np.array([qx[shift_index]]))
#         qy = np.append(qy, np.array([-qy[shift_index]]))
#         S_plot = np.append(S_plot, np.array([S_plot[shift_index]]))
#
#     right_edge = [114,130,146,162,196,212]
#     for shift_index in right_edge:
#         qx = np.append(qx, np.array([qx[shift_index]]))
#         qy = np.append(qy, np.array([-qy[shift_index]]))
#         S_plot = np.append(S_plot, np.array([S_plot[shift_index]]))
#
#     """""""""""""""""""""""""""""""""""""""
#     Plot scatter
#     """""""""""""""""""""""""""""""""""""""
#
#     if divide:
#         im = ax[0,ii].scatter(qx, qy, c=abs(S_plot), s=ms, cmap='seismic', norm=colors.TwoSlopeNorm(vcenter = 1, vmin = 0.0, vmax=3.53))
#     else:
#         im = ax[0,ii].scatter(qx, qy, c=abs(S_plot), s=ms, cmap='gist_heat',  norm=colors.LogNorm(vmin=5e-7, vmax=1))
#     # colorbar
#     if SRT == 25:
#         if divide:
#             ticks=[0.0, 0.25,0.5, 0.75, 1.0, 1.5, 2.0,2.5,3.0,3.5]
#             cb = fig.colorbar(im, ax=ax, aspect=15, ticks=ticks)
#             cb.ax.tick_params(labelsize=cb_ticks_font_size)
#             cb.ax.set_yticklabels(ticks)  # vertically oriented colorbar
#         else:
#             cb = fig.colorbar(im, ax=ax[0,ii], aspect=10)
#             cb.ax.tick_params(labelsize=cb_ticks_font_size)
#
#
#
#     ax[0,ii].axis('off')
#     ax[0,ii].text(0.01, 0.9, '(%s)' % (panel), transform=ax[0,ii].transAxes,
#                 size=fs_panel, color = 'black')
#     ax[0,ii].text(0.8, 0.9, '%3.fK' % T_list[SRT],size=fs_panel-2,
#     transform=ax[0,ii].transAxes, color = 'black')
#
#
#     plt.tick_params(top=False, bottom=False, left=False, right=False,
#                     labelleft=False, labelbottom=False)
                    
"""""""""""""""""""""""""""""""""""""""
SECOND ROW!
"""""""""""""""""""""""""""""""""""""""

# divide = False
# class_exponent = 0
# quant_exponent = -1
# save = 'quant'
# BZ_color = 'k'
# panel_label_list = ['d', 'e', 'f']
#
# for ii,(SRT,panel) in enumerate(zip(SRT_list,panel_label_list)):
#
#     print(SRT)
#
#     """""""""""""""""""""""""""""""""""""""
#     Load structure factor
#     """""""""""""""""""""""""""""""""""""""
#
#     S_tmp = np.load('S_TaS2_18x18_N_steps_start=70_N_steps_inter=10_N_steps_end=1056_CLASSICAL/S_%d.npy' % SRT)
#     S['class'] = (S_tmp.sum(axis=0)).reshape(N1*N1) / S_tmp.shape[0]
#
#     S_tmp = np.load('S_TaS2_18x18_N_steps_start=70_N_steps_inter=10_N_steps_end=496_PIMD_beads/S_%d.npy' % SRT)
#     S['quant'] = (S_tmp.sum(axis=0)).reshape(N1*N1) / S_tmp.shape[0]
#
#     S_tmp = np.load('S_TaS2_18x18_N_steps_start=70_N_steps_inter=10_N_steps_end=1056_CLASSICAL/S_%d_BG.npy' % SRT)
#     S['class_BG'] = (S_tmp.sum(axis=0)).reshape(N1*N1) / S_tmp.shape[0]
#
#     S_tmp = np.load('S_TaS2_18x18_N_steps_start=70_N_steps_inter=10_N_steps_end=496_PIMD_beads/S_%d_BG.npy' % SRT)
#     S['quant_BG'] = (S_tmp.sum(axis=0)).reshape(N1*N1) / S_tmp.shape[0]
#
# #    S['class'] = S['class_BG']
# #    S['quant'] = S['quant_BG']
#
#     """""""""""""""""""""""""""""""""""""""
#     Draw Brillouin zone
#     """""""""""""""""""""""""""""""""""""""
#
#     outline = elphmod.bravais.BZ()
#     outline = np.array(outline) / (a / nk)
#     outline = list(outline)
#
#     ax[1,ii].fill_between(*zip(*outline), color = BZ_color)
#     ax[1,ii].plot(*zip(*outline), color='gray',
#     linewidth = 1, alpha=0.4)
#
#     """""""""""""""""""""""""""""""""""""""
#     Choose quantity to plot
#     """""""""""""""""""""""""""""""""""""""
#
#     S_plot = S['class']**(class_exponent) / S['quant']**(quant_exponent)
#
#
#     """""""""""""""""""""""""""""""""""""""
#     Add BZ points from the edge
#     """""""""""""""""""""""""""""""""""""""
#
#     q = np.load('output_kpoints/q_voronoi_%s%s2_%dx%d.npy' % ('Ta','S',N1,N1))
#     q = np.reshape(q,(N1*N1,3))
#     qx = q[:,0] / (2*np.pi)
#     qy = q[:,1] / (2*np.pi)
#
#
#     # K points
#     qx = np.append(qx, np.array([-1.96841415e-01]))
#     qy = np.append(qy, np.array([0]))
#     S_plot = np.append(S_plot, np.array([S_plot[228]]))
#
#     qx = np.append(qx, np.array([1.96841415e-01]))
#     qy = np.append(qy, np.array([0]))
#     S_plot = np.append(S_plot, np.array([S_plot[228]]))
#
#     upper_edge = [228,263,298,9,44,79,114]
#     for shift_index in upper_edge:
#         qx = np.append(qx, np.array([qx[shift_index]]))
#         qy = np.append(qy, np.array([-qy[shift_index]]))
#         S_plot = np.append(S_plot, np.array([S_plot[shift_index]]))
#
#     left_edge = [133,152,171,190,209,79,114,228]
#     for shift_index in left_edge:
#         qx = np.append(qx, np.array([qx[shift_index]]))
#         qy = np.append(qy, np.array([-qy[shift_index]]))
#         S_plot = np.append(S_plot, np.array([S_plot[shift_index]]))
#
#     right_edge = [114,130,146,162,196,212]
#     for shift_index in right_edge:
#         qx = np.append(qx, np.array([qx[shift_index]]))
#         qy = np.append(qy, np.array([-qy[shift_index]]))
#         S_plot = np.append(S_plot, np.array([S_plot[shift_index]]))
#
#     """""""""""""""""""""""""""""""""""""""
#     Plot scatter
#     """""""""""""""""""""""""""""""""""""""
#
#     if divide:
#         im = ax[1,ii].scatter(qx, qy, c=abs(S_plot), s=ms, cmap='seismic', norm=colors.TwoSlopeNorm(vcenter = 1, vmin = 0.0, vmax=3.53))
#     else:
#         im = ax[1,ii].scatter(qx, qy, c=abs(S_plot), s=ms, cmap='gist_heat',  norm=colors.LogNorm(vmin=5e-7, vmax=1))
#     # colorbar
#     if SRT == 25:
#         if divide:
#             ticks=[0.0, 0.25,0.5, 0.75, 1.0, 1.5, 2.0,2.5,3.0,3.5]
#             cb = fig.colorbar(im, ax=ax, aspect=15, ticks=ticks)
#             cb.ax.tick_params(labelsize=cb_ticks_font_size)
#             cb.ax.set_yticklabels(ticks)  # vertically oriented colorbar
#         else:
#             cb = fig.colorbar(im, ax=ax[1,ii], aspect=10)
#             cb.ax.tick_params(labelsize=cb_ticks_font_size)
#
#
#
#     ax[1,ii].axis('off')
#     ax[1,ii].text(0.01, 0.9, '(%s)' % (panel), transform=ax[1,ii].transAxes,
#                 size=fs_panel, color = 'black')
#     ax[1,ii].text(0.8, 0.9, '%3.fK' % T_list[SRT],size=fs_panel-2,
#     transform=ax[1,ii].transAxes, color = 'black')
#
#
#     plt.tick_params(top=False, bottom=False, left=False, right=False,
#                     labelleft=False, labelbottom=False)
                    
"""""""""""""""""""""""""""""""""""""""
THIRD ROW!
"""""""""""""""""""""""""""""""""""""""

divide = True
class_exponent = 1
quant_exponent = 1
save = 'division'
BZ_color = 'white'
panel_label_list = ['a', 'b', 'c']
                    
for ii,(SRT,panel) in enumerate(zip(SRT_list,panel_label_list)):
                    
    print(SRT)
    
    """""""""""""""""""""""""""""""""""""""
    Load structure factor
    """""""""""""""""""""""""""""""""""""""

    S_tmp = np.load('S_TaS2_18x18_N_steps_start=70_N_steps_inter=10_N_steps_end=1056_CLASSICAL/S_%d.npy' % SRT)
    S['class'] = (S_tmp.sum(axis=0)).reshape(N1*N1) / S_tmp.shape[0]

    S_tmp = np.load('S_TaS2_18x18_N_steps_start=70_N_steps_inter=10_N_steps_end=496_PIMD_beads/S_%d.npy' % SRT) 
    S['quant'] = (S_tmp.sum(axis=0)).reshape(N1*N1) / S_tmp.shape[0]

    S_tmp = np.load('S_TaS2_18x18_N_steps_start=70_N_steps_inter=10_N_steps_end=1056_CLASSICAL/S_%d_BG.npy' % SRT)
    S['class_BG'] = (S_tmp.sum(axis=0)).reshape(N1*N1) / S_tmp.shape[0]

    S_tmp = np.load('S_TaS2_18x18_N_steps_start=70_N_steps_inter=10_N_steps_end=496_PIMD_beads/S_%d_BG.npy' % SRT) 
    S['quant_BG'] = (S_tmp.sum(axis=0)).reshape(N1*N1) / S_tmp.shape[0]

#    S['class'] = S['class_BG']
#    S['quant'] = S['quant_BG']
    
    """""""""""""""""""""""""""""""""""""""
    Draw Brillouin zone
    """""""""""""""""""""""""""""""""""""""

    outline = elphmod.bravais.BZ() 
    outline = np.array(outline) / (a / nk)
    outline = list(outline)

    ax[ii].fill_between(*zip(*outline), color = BZ_color)
    ax[ii].plot(*zip(*outline), color='gray',
    linewidth = 1, alpha=0.4)
    
    """""""""""""""""""""""""""""""""""""""
    Choose quantity to plot
    """""""""""""""""""""""""""""""""""""""

    S_plot = S['class']**(class_exponent) / S['quant']**(quant_exponent) 


    """""""""""""""""""""""""""""""""""""""
    Add BZ points from the edge
    """""""""""""""""""""""""""""""""""""""

    q = np.load('output_kpoints/q_voronoi_%s%s2_%dx%d.npy' % ('Ta','S',N1,N1))
    q = np.reshape(q,(N1*N1,3))
    qx = q[:,0] / (2*np.pi)
    qy = q[:,1] / (2*np.pi)
    

    # K points
    qx = np.append(qx, np.array([-1.96841415e-01]))
    qy = np.append(qy, np.array([0]))
    S_plot = np.append(S_plot, np.array([S_plot[228]]))
    
    qx = np.append(qx, np.array([1.96841415e-01]))
    qy = np.append(qy, np.array([0]))
    S_plot = np.append(S_plot, np.array([S_plot[228]]))
    
    upper_edge = [228,263,298,9,44,79,114]
    for shift_index in upper_edge:
        qx = np.append(qx, np.array([qx[shift_index]]))
        qy = np.append(qy, np.array([-qy[shift_index]]))
        S_plot = np.append(S_plot, np.array([S_plot[shift_index]]))

    left_edge = [133,152,171,190,209,79,114,228]
    for shift_index in left_edge:
        qx = np.append(qx, np.array([qx[shift_index]]))
        qy = np.append(qy, np.array([-qy[shift_index]]))
        S_plot = np.append(S_plot, np.array([S_plot[shift_index]]))
        
    right_edge = [114,130,146,162,196,212]
    for shift_index in right_edge:
        qx = np.append(qx, np.array([qx[shift_index]]))
        qy = np.append(qy, np.array([-qy[shift_index]]))
        S_plot = np.append(S_plot, np.array([S_plot[shift_index]]))
    
    """""""""""""""""""""""""""""""""""""""
    Plot scatter
    """""""""""""""""""""""""""""""""""""""

    if divide:
        im = ax[ii].scatter(qx, qy, c=abs(S_plot), s=ms, cmap='seismic', norm=colors.TwoSlopeNorm(vcenter = 1, vmin = 0.0, vmax=3.53))
    else:
        im = ax[ii].scatter(qx, qy, c=abs(S_plot), s=ms, cmap='gist_heat',  norm=colors.LogNorm(vmin=5e-7, vmax=1))
    # colorbar
    if SRT == 25:
        if divide:
            ticks=[0.0, 0.25,0.5, 0.75, 1.0, 1.5, 2.0,2.5,3.0,3.5]
            cb = fig.colorbar(im, ax=ax[ii], aspect=10, ticks=ticks)
            cb.ax.tick_params(labelsize=cb_ticks_font_size)
            cb.ax.set_yticklabels(ticks)  # vertically oriented colorbar



    ax[ii].axis('off')
    ax[ii].text(0.01, 0.9, '(%s)' % (panel), transform=ax[ii].transAxes,
                size=fs_panel, color = 'black')
    ax[ii].text(0.8, 0.9, '%3.fK' % T_list[SRT],size=fs_panel-2,
    transform=ax[ii].transAxes, color = 'black')


    plt.tick_params(top=False, bottom=False, left=False, right=False,
                    labelleft=False, labelbottom=False)   


plt.tight_layout()
plt.savefig('fig_cdw_abc.pdf')
#plt.savefig('fig9_paper.png')
#    plt.show()
#    plt.close()


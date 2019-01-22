#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 14:56:51 2019

@author: Francis-Yan Cyr-Racine

"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# Generic properties from matplotlib
rcParams['font.family'] = 'serif'
rcParams['text.usetex'] = True

def convert_ax_c_to_l(ax_f):
    """
    Update second axis according with first axis.
    """
    y1, y2 = ax_f.get_xlim()
    ax_c.set_xlim(y1, y2)
    ax_c.figure.canvas.draw()

# Load data
WDM_array_LSST = np.genfromtxt('plot_data/WDM_array_LSST.txt')
som_array_LSST = np.genfromtxt('plot_data/som_array_LSST.txt')
N_sat_LSST = np.genfromtxt('plot_data/N_sat_LSST.txt')

WDM_array_SDSS = np.genfromtxt('plot_data/WDM_array_SDSS.txt')
som_array_SDSS = np.genfromtxt('plot_data/som_array_SDSS.txt')
N_sat_SDSS = np.genfromtxt('plot_data/N_sat_SDSS.txt')

fig2, ax2 = plt.subplots(figsize=(10, 6))
ax_c = ax2.twiny()
ax2.callbacks.connect("xlim_changed", convert_ax_c_to_l)

# Stellar stream region
ax2.axvspan(0.5,25,color='gray',alpha=0.3)

# LSST projected sensitivity
level_LSST = 92
ax2.contourf(WDM_array_LSST[:20],som_array_LSST,N_sat_LSST.T[:,:20],[0,106],colors='#85C1E9',alpha=0.6)
ax2.contourf(WDM_array_LSST[19:,],som_array_LSST,N_sat_LSST.T[:,19:],[0,level_LSST],colors=['#85C1E9'],alpha=0.6)
ax2.contour(WDM_array_LSST[19:],som_array_LSST[:35],N_sat_LSST.T[:35,19:],[level_LSST],colors=['k'],linewidths=1)
ax2.contour(WDM_array_LSST[19:],som_array_LSST[35:],N_sat_LSST.T[35:,19:],[level_LSST],colors=['k'],linestyles='dashed',linewidths=1)

# SDSS limits
ax2.contour(WDM_array_SDSS,som_array_SDSS,N_sat_SDSS.T,[43],colors=['k'],linewidths=1)
ax2.contourf(WDM_array_SDSS,som_array_SDSS,N_sat_SDSS.T,[0,43],colors=['#FA0303'],alpha=1)

# Other limits and sensitivities
ax2.axvline(5.3,c='k',ls='--',lw=0.6) #Lyman-alpha
ax2.axvline(8,c='k',ls='--',lw=0.6) #lensing
ax2.axvline(25,c='k',ls='--',lw=0.6) #streams
ax2.axvline(7.59,0.805,1,c='k',ls='--',lw=1) #minimum halo mass
ax2.axvline(7.59,0,.257,c='k',lw=1) #minimum halo mass

# Text labels
ax2.text(4.7,0.09,r'Lyman-$\alpha$ ($95\%$ C.L.)',fontsize=10,rotation='vertical')
ax2.text(7.3,1.6,r'Substructure Lensing (100 lenses)',fontsize=10,rotation='vertical')
ax2.text(0.9,4.7,r'Excluded by classical + SDSS MW Sats.',fontsize=16,rotation='vertical')
ax2.text(12,0.02,r'Probed by LSST streams',fontsize=16)
ax2.text(12,5.1,r'Probed by LSST Streams',fontsize=16)
ax2.text(11,0.35,r'Probed by MW Sats. + Spec.',fontsize=16)
ax2.text(10.5,2.45,r'Approx. sensitivity of MW Sats. w/ core collapse',fontsize=10)

# axes, ticks, and labels
ax2.set_yscale('log')
ax2.set_xlabel(r'$m_{\rm WDM}\,({\rm keV})$', fontsize=20)
ax2.set_ylabel(r'$\sigma_{\rm SIDM}/m_\chi\,({\rm cm^2 g^{-1}})$', fontsize=20)
ax_c.set_xlabel(r'$M_{\rm hm}\, ({\rm M}_\odot)$',size = 20)
ax2.set_xticks([5,10,15,20,25,30])
ax_c.set_xticklabels([r'$10^10$',r'$2.6\times10^8$',r'$2.6\times10^7$',r'$6.7\times10^6$',r'$2.5\times10^6$',r'$1.2\times10^6$',r'$6.6\times10^5$'],fontdict = {'fontsize':15})

ticklabels = ax2.get_xticklabels()
ticklabels.extend(ax2.get_yticklabels())
for label in ticklabels:
    label.set_color('k')
    label.set_fontsize(20)

fig2.savefig('SIDM_WDM_figw_coll.pdf',bbox_inches='tight')
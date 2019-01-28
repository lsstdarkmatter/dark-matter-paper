#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 14:56:51 2019

@author: Francis-Yan Cyr-Racine

"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
import matplotlib
from lsstplot import get_datafile, COLORS, ALPHA

# Generic properties from matplotlib
rcParams['font.family'] = 'serif'
rcParams['text.usetex'] = True
rcParams['hatch.linewidth'] = 5.0

BLUE = COLORS['blue']
RED  = COLORS['red']

def convert_ax_c_to_l(ax_f):
    """
    Update second axis according with first axis.
    """
    y1, y2 = ax_f.get_xlim()
    ax_c.set_xlim(y1, y2)
    ax_c.figure.canvas.draw()

def latex_float(f):
    """
    Convert float to latex format. See:
    https://stackoverflow.com/a/13490601
    """
    float_str = "{0:.2g}".format(f)
    if "e" in float_str:
        base, exponent = float_str.split("e")
        return r"${0} \times 10^{{{1}}}$".format(base, int(exponent))
    else:
        return r"$%s$"%(float_str)

def mwdm2mhalo(mwdm):
    """
    Convert from warm dark matter particle mass to halo mass
    From Bullock & Boylan-Kolchin 2017

    Parameters:
    -----------
    mwdm : warm dark matter particle mass (keV)

    Returns:
    --------
    mhalo : halo mass (Msun)
    """
    return 5.5e10*(np.asarray(mwdm)/1.0)**-3.33

def mhalo2mwdm(mhalo):
    """
    Convert from halo mass to warm dark matter particle mass
    From Bullock & Boylan-Kolchin 2017

    Parameters:
    -----------
    mhalo : halo mass (Msun)

    Returns:
    --------
    mwdm : warm dark matter particle mass (keV)
    """
    return (np.asarray(mhalo)/5.5e10)**(1/-3.33)


# Load data
WDM_array_LSST = np.genfromtxt(get_datafile('WDM_array_LSST.txt'))
som_array_LSST = np.genfromtxt(get_datafile('som_array_LSST.txt'))
N_sat_LSST = np.genfromtxt(get_datafile('N_sat_LSST.txt'))

WDM_array_SDSS = np.genfromtxt(get_datafile('WDM_array_SDSS.txt'))
som_array_SDSS = np.genfromtxt(get_datafile('som_array_SDSS.txt'))
N_sat_SDSS = np.genfromtxt(get_datafile('N_sat_SDSS.txt'))

fig2, ax2 = plt.subplots(figsize=(10, 6))
ax_c = ax2.twiny()
ax2.callbacks.connect("xlim_changed", convert_ax_c_to_l)

# Stellar stream region
#ax2.axvspan(0.5,18,color='gray',alpha=0.3)

# LSST projected sensitivity
level_LSST = 92
ax2.contour(WDM_array_LSST[19:],som_array_LSST[35:],N_sat_LSST.T[35:,19:],[level_LSST],colors=['k'],linestyles='dashed',linewidths=1)
ax2.contourf(WDM_array_LSST[:20],som_array_LSST,N_sat_LSST.T[:,:20],[0,106],colors=BLUE,alpha=ALPHA)
ax2.contourf(WDM_array_LSST[19:,],som_array_LSST,N_sat_LSST.T[:,19:],[0,level_LSST],colors=BLUE,alpha=ALPHA)
ax2.contour(WDM_array_LSST[19:],som_array_LSST[:35],N_sat_LSST.T[:35,19:],[level_LSST],colors=['k'],linewidths=1)
# Upper collapse region (som > 1 cm2/g)
ax2.contourf(WDM_array_LSST[19:,],som_array_LSST[46:],N_sat_LSST.T[46:,19:],[level_LSST,np.inf],colors=BLUE,alpha=ALPHA/3.)

# Can get contour lines with...
#x,y = cs.collections[0].get_paths()[0].vertices.T
#plt.fill_between(x,y,y2=10,alpha=0.6,facecolor="none", hatch="/", edgecolor='#85C1E9',zorder=0,lw=0)
#plt.fill_between(x,y,y2=10,alpha=0.3,facecolor='tab:blue')

# SDSS limits
ax2.contour(WDM_array_SDSS,som_array_SDSS,N_sat_SDSS.T,[43],colors=['k'],linewidths=1)
ax2.contourf(WDM_array_SDSS,som_array_SDSS,N_sat_SDSS.T,[0,43],colors=[RED],alpha=1)

# Other limits and sensitivities
ax2.axvline(5.3,c='k',dashes=(5,2),lw=0.6) #Lyman-alpha
ax2.axvline(8,c='k',dashes=(5,2),lw=0.6) #lensing
ax2.axvline(18,c='k',dashes=(5,2),lw=0.6) #streams
ax2.axvline(7.59,0.805,1,c='k',ls='--',lw=1) #minimum halo mass
ax2.axvline(7.59,0,.257,c='k',lw=1) #minimum halo mass

# Text labels
ax2.text(4.7,0.09,r'Lyman-$\alpha$ ($95\%$ C.L.)',fontsize=10,rotation='vertical')
ax2.text(7.3,1.6,r'LSST Strong Lensing (100 lenses)',fontsize=10,rotation='vertical')
ax2.text(17.4,1.0,r'LSST Stellar Streams',fontsize=10,rotation='vertical')
ax2.text(1.3,4.7,r'Excluded by classical + SDSS MW Sats.',fontsize=16,rotation='vertical')
#ax2.text(10,0.02,r'Probed by LSST streams',fontsize=16)
#ax2.text(10,5.1,r'Probed by LSST Streams',fontsize=16)
ax2.text(12,0.45,r'Probed by LSST',fontsize=16,ha='center')
ax2.text(12,0.32,r'MW Sats. + Spec.',fontsize=16,ha='center')
ax2.text(9,2.45,r'Approx. sensitivity of MW Sats. w/ core collapse',fontsize=10)

# axes, ticks, and labels
ax2.set_yscale('log')
ax2.set_xlabel(r'$m_{\rm WDM}\,({\rm keV})$', fontsize=20)
ax2.set_ylabel(r'$\sigma_{\rm SIDM}/m_\chi\,({\rm cm^2 g^{-1}})$', fontsize=20)
ax_c.set_xlabel(r'$M_{\rm hm}\, ({\rm M}_\odot)$',size = 20)

ax2.set_xlim(0.5,22)

xticks = [5,10,15,20]
ticklabels = [latex_float(x) for x in mwdm2mhalo(xticks)]

ax2.set_xticks(xticks)
ax_c.set_xticks(xticks)
ax_c.set_xticklabels(ticklabels)

ticklabels = ax2.get_xticklabels()
ticklabels.extend(ax2.get_yticklabels())
for label in ticklabels:
    label.set_color('k')
    label.set_fontsize(20)

fig2.savefig('SIDM_WDM_figw_coll.pdf',bbox_inches='tight')

#!/usr/bin/env python
"""
Plot warm dark matter mass vs self-interaction scattering cross section.
"""
import pylab as plt
import numpy as np
from matplotlib.ticker import MaxNLocator, LogLocator

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

fig,ax = plt.subplots()
ax2 = ax.twiny()
plt.sca(ax)

ax.set_yscale('log')
ax.set_xscale('log')
ax2.set_xscale('log')

plt.axvline(3,ls='--',lw=2,color='r')
plt.axhline(1,ls='--',lw=2,color='r')

plt.xlim(0.1,100)
plt.ylim(0.01,10)
plt.xlabel(r'$m_{\rm WDM}$ (keV)')
plt.ylabel(r'$\sigma_{\rm SIDM} {\rm (cm^2 g^{-1})}$')

ax2.set_xlim(mwdm2mhalo(np.array(ax.get_xlim())))
#ax2.xaxis.set_major_locator(LogLocator(numticks=6,prune='left'))
ax2.set_xlabel(r'Halo Mass ($M_\odot$)')

plt.savefig('wdm_sidm.pdf')

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

##########################################
# Plot the data

plt.axvline(3,ls='--',lw=2,color='r')
plt.axhline(1,ls='--',lw=2,color='r')

# This is just an example for illustration...
mwdm = np.logspace(np.log10(3),2,100)
plt.plot(mwdm, -1.0/(mwdm-2)**0.5 + 1, color='dodgerblue', lw=3)

##########################################

plt.xlim(0.1,100)
plt.ylim(0.01,10)
ax2.set_xlim(mwdm2mhalo(np.array(ax.get_xlim())))

plt.xlabel(r'${\rm Particle\ Mass\ (keV)}$',fontsize=20)
plt.ylabel(r'$\sigma_{\rm SIDM}\ {\rm (cm^2 g^{-1})}$',fontsize=20)
ax2.set_xlabel(r'${\rm Halo\ Mass\ (M_\odot)}$',fontsize=20)

# This is "necessary" to get the ax2 labels...
plt.savefig('wdm_sidm.pdf')

ticklabels = ['' if i%2 else t.get_text() for i,t in enumerate(ax2.get_xticklabels())]
ax2.set_xticklabels(ticklabels)
plt.savefig('wdm_sidm.pdf')

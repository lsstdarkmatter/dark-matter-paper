#!/usr/bin/env python
"""
Plot dark matter mass vs indirect detection annihilation cross section.
"""
import pylab as plt
import numpy as np
import yaml

from lsstplot import plot_limit,plot_limit_fill,plot_limit_patch,plot_lsst_limit
from lsstplot import get_mass_limit,get_datafile

def create_projection():
    mass,limit = get_mass_limit(limits['ackermann15_bb'])
    #mass,limit = np.genfromtxt(StringIO(data['xystring'])).T
    # Now for the projection factors
    proj_factor = np.ones(len(limit))

    # 1) @apace predicts that the integrated J-factor could increase by ~3x
    proj_factor *= 3
    # 2) We expect to have ~18 years of data
    proj_factor *= 3
    # 3) the limits will scale as N^(1/2) at low mass and N^(1) at high mass
    # We fit to the curve in Fig 16 in 1605.02016
    slope = (0.5 - 0.75)/ (np.log10(6) - np.log10(1e4))
    fn = lambda mass: slope * np.log10(mass) + 0.43

    proj_factor = proj_factor**(-fn(mass))
    proj = proj_factor * limit
    return mass, proj

fig,ax = plt.subplots()
ax.set_yscale('log')
ax.set_xscale('log')
plt.axhline(3e-26,ls='--',lw=2,color='gray')

limits = yaml.load(open(get_datafile('ann_limits.yaml')))

## Print the projected sensitivity
#for m,l in zip(*create_projection()):
#    print('%-10i %12.8g'%(m, l))

plot_lsst_limit(limits['lsst_dwarfs_bb'])

plot_limit_fill(limits['ackermann15_bb'])
plot_limit_fill(limits['hess_gc_einasto_2016_bb_95cl'])
plot_limit_fill(limits['zaharijas2018_cta_bb'])
plot_limit_patch(limits['gc_summary_bb_1s'])

plt.xlim(1,1e4)
plt.ylim(5e-28,1e-23)
#plt.xlabel(r'$m_{\rm DM}$ (GeV)',fontsize=18)
#plt.ylabel(r'$\langle \sigma_{\rm ann} v \rangle {\rm (cm^3 s^{-1})}$',fontsize=18)
plt.xlabel(r'Dark Matter Mass (GeV)',fontsize=18)
plt.ylabel(r'Dark Matter Annihilation Cross Section (cm$^3$ s$^{-1}$)',fontsize=18)
plt.subplots_adjust(top=0.95,bottom=0.12)

plt.annotate(r'$\chi \chi \rightarrow b \bar b$', xy=(2e3,1e-27),fontsize=24)

plt.savefig('annih_limits.pdf')
plt.ion()

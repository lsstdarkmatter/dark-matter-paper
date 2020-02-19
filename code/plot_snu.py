#!/usr/bin/env python
"""
Generic python script.
"""
__author__ = "Alex Drlica-Wagner"
import copy
import pylab as plt
import numpy as np
import yaml

from lsstplot import plot_limit, plot_limit_fill, plot_limit_patch, plot_lsst_limit
import lsstplot

def m22_nu(m22):
    return 1e-6 * (m22/40)

def nu_m22(nu):
    return  40 * nu / 1e-6

limits = yaml.load(open('data/snu_limits.yaml'))

fig,ax = plt.subplots()
ax.set_yscale('log')
ax.set_xscale('log')

m,l = lsstplot.get_mass_limit(limits['schneider2016_sats'])

plot_limit_fill(limits['tremaine_gunn'])
plot_limit(limits['tremaine_gunn'])

#plot_limit_fill(limits['schneider2016_nonres'])
#plot_limit(limits['schneider2016_notdm'])

plot_limit_fill(limits['merle2017_katrin'],alpha=0.1)
plot_limit(limits['merle2017_katrin'],linestyle='--',alpha=0.7)

#plot_limit_fill(limits['merle2017_dy163_phaseI'],alpha=0.1)
#plot_limit(limits['merle2017_dy163_phaseI'],linestyle='--',alpha=0.7)

#plot_limit_fill(limits['merle2017_dy163_phaseII'],alpha=0.1)
#plot_limit(limits['merle2017_dy163_phaseII'],linestyle='--',alpha=0.7)

plot_limit_fill(limits['merle2017_xray'],alpha=0.1)
plot_limit(limits['merle2017_xray'])

plot_limit_fill(limits['schneider2016_sats'],alpha=0.5)
#plot_limit(limits['schneider2016_lya_v13'])
#plot_limit_fill(limits['schneider2016_lya_b15'])
#plot_lsst_limit(limits['schneider2016_lya_b15'])

plot_lsst_limit(limits['lsst_streams'],alpha=0.3)

plot_limit_fill(limits['merle2017_overprod'])
plot_limit(limits['merle2017_overprod'])



ax.set_xlim(0.3,50)
ax.set_ylim(1e-12,1e-2)

#ax.set_yticks([1e-12,1e-9,1e-6,1e-3])

ax.set_xticks([0.5,1,5,10,50])
ax.set_xticklabels([0.5,1,5,10,50],fontsize=18)

ax.set_xlabel(r'Sterile Neutrino Mass (keV)',fontsize=18)
ax.set_ylabel(r'$\sin^2(2\theta)$',fontsize=18)

plt.subplots_adjust(top=0.90,bottom=0.12)


plt.savefig('snu_limits.pdf')
plt.savefig('snu_limits.png')
plt.ion()

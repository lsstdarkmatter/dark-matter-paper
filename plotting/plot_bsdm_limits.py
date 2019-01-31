#!/usr/bin/env python
"""
Generic python script.
"""
__author__ = "Alex Drlica-Wagner"
import pylab as plt
import numpy as np
import yaml

from lsstplot import plot_limit, plot_limit_fill, plot_limit_patch, plot_lsst_limit

limits = yaml.load(open('data/bsdm_limits.yaml'))

fig,ax = plt.subplots()
ax.set_yscale('log')
ax.set_xscale('log')

plot_lsst_limit(limits['lsst_dwarfs'])

plot_limit_fill(limits['gluscevic2018_planck'])
plot_limit_patch(limits['emken2018_cresst3_dd'])
plot_limit_patch(limits['erickcek2007_xqc'])
#plot_limit_patch(limits['mahdawi2019_xqc_e1'])
plot_limit_patch(limits['bringmann2018_xenon1t'])
plot_limit_patch(limits['bringmann2018_miniboone'])


plt.xlim(1e-5,1e1)
plt.ylim(1e-34,1e-24)
plt.xlabel(r'Dark Matter Mass (GeV)',fontsize=18)
plt.ylabel(r'Dark Matter Scattering Cross Section (cm$^2$)',fontsize=18)
plt.subplots_adjust(top=0.95,bottom=0.12)

plt.savefig('bsdm_limits.pdf')
plt.ion()


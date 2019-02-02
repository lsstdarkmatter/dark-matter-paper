#!/usr/bin/env python
"""
Plot dark matter mass vs indirect detection annihilation cross section.
"""
import pylab as plt
import numpy as np
import yaml

from lsstplot import plot_one, plot_two, plot_limit, plot_lsst_limit

fig,ax = plt.subplots()
ax.set_yscale('log')
ax.set_xscale('log')

limits = yaml.load(open('./data/macho_limits.yaml'))

#plot_limit(limits['lsst_m31_microlensing'])
#plot_limit(limits['lsst_paralensing'])
#plot_limit(limits['lsst_microlensing'])

plot_lsst_limit(limits['lsst_microlensing'])
plot_limit(limits['lsst_paralensing'])


plot_two(limits['gammaray_background_loose_carr_2016'],
         limits['gammaray_background_tight_carr_2016'])
plot_one(limits['gammaray_femtolens_carr_2016'])
plot_two(limits['ns_capture_loose_capela_2013'],
         limits['ns_capture_tight_capela_2013'])
plot_one(limits['hsc_niikura_2017'])
plot_two(limits['eridanus_brandt_2016_loose'],
         limits['eridanus_brandt_2016_tight'])
plot_two(limits['lensed_sn_garcia-bellido_2017_loose'],
         limits['lensed_sn_zumalacarregui_2018_tight'])
plot_two(limits['lensed_sn_garcia-bellido_2017_loose'],
         limits['lensed_sn_zumalacarregui_2018_tight'])
plot_one(limits['eros_tisserand_2007'])
plot_two(limits['binaries_quinn_2009_loose'],
         limits['binaries_yoo_2003_tight'])
plot_two(limits['plank_ali-haimoud_2016_loose'],
         limits['cmb_ricotti_2008_tight'])
plot_one(limits['disk_lacey_1985'])

plt.xlim(1e-18, 1e8)
plt.ylim(1e-4, 1.0)
plt.xlabel(r'${\rm Compact\ Object\ Mass}\ (M_\odot)$',fontsize=18)
plt.ylabel(r'${\rm Dark\ Matter\ Fraction}$', fontsize=18)
plt.subplots_adjust(top=0.95, bottom=0.12)

plt.savefig('macho_limits.pdf')
plt.ion()

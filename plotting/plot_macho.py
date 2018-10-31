#!/usr/bin/env python
"""
Plot dark matter mass vs indirect detection annihilation cross section.
"""
import pylab as plt
import numpy as np
import yaml
from StringIO import StringIO
from matplotlib.patches import Ellipse

def plot_limit(section):
    data = limits[section]
    mass,limit = np.genfromtxt(StringIO(data['xystring'])).T
    if data['mass_unit'] == 'gram':
        mass /= 2e33
    kwargs = dict(**data['style'])
    plt.plot(mass,limit,**kwargs)

fig,ax = plt.subplots()
ax.set_yscale('log')
ax.set_xscale('log')

limits = yaml.load(open('data/macho_limits.yaml'))

plot_limit('macho_alcock_2001')
plot_limit('eros_tisserand_2007')
plot_limit('eridanus_li_2016')
plot_limit('kepler_griest_2013')
plot_limit('hsc_niikura_2017')
plot_limit('binaries_quinn_2009')
plot_limit('disk_lacey_1985')
plot_limit('binaries_yoo_2003')
plot_limit('gammaray_femtolens_carr_2016')
plot_limit('ns_capture_optimistic_capela_2013')

plt.xlim(1e-18,1e17)
plt.ylim(1e-5,1.0)
plt.xlabel(r'${\rm Compact\ Object\ Mass}\ (M_\odot)$',fontsize=18)
plt.ylabel(r'${\rm Dark\ Matter\ Fraction}$',fontsize=18)
plt.subplots_adjust(top=0.95,bottom=0.12)


#plt.annotate(r'$\chi \chi \rightarrow b \bar b$', xy=(2e3,1e-27),fontsize=24)

plt.savefig('macho_limits.pdf')
plt.ion()

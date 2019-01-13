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
    plt.plot(mass, limit, **kwargs)
    # plt.plot(mass, limit, '.')
    # x_label = np.median(mass)
    # y_label = np.min(limit)
    # plt.text(x_label, y_label, data['style']['label'],
    #          horizontalalignment='center',
    #          verticalalignment='top')
    plt.text(float(data['label_x']),
             float(data['label_y']),
             data['style']['label'],
             horizontalalignment='center',
             verticalalignment='top')

def plot_one(section):
    data = limits[section]
    mass,limit = np.genfromtxt(StringIO(data['xystring'])).T
    if data['mass_unit'] == 'gram':
        mass /= 2e33
    kwargs = dict(**data['style'])
    plt.fill_between(mass, limit, y2=1.0,
                     edgecolor='tab:blue',
                     facecolor='tab:blue',
                     alpha=0.3)
    plt.text(float(data['label_x']),
             float(data['label_y']),
             data['style']['label'],
             horizontalalignment='center',
             verticalalignment='top')

def plot_two(section_loose, section_tight):
    data_loose = limits[section_loose]
    mass_loose,limit_loose = np.genfromtxt(StringIO(data_loose['xystring'])).T
    if data_loose['mass_unit'] == 'gram':
        mass_loose /= 2e33

    data_tight = limits[section_tight]
    mass_tight,limit_tight = np.genfromtxt(StringIO(data_tight['xystring'])).T
    if data_tight['mass_unit'] == 'gram':
        mass_tight /= 2e33

    # Interpolate the data to a common grid
    x_min = np.min((np.min(mass_loose), np.min(mass_tight)))
    x_max = np.max((np.max(mass_loose), np.max(mass_tight)))
    x = np.logspace(np.log10(x_min), np.log10(x_max), num=100)
    limit_loose_interp = np.interp(x, mass_loose, limit_loose)
    limit_tight_interp = np.interp(x, mass_tight, limit_tight)

    plt.fill_between(mass_loose, limit_loose, y2=1.0,
                     edgecolor='tab:blue',
                     facecolor='tab:blue',
                     alpha=0.3)
    plt.fill_between(x, limit_tight_interp, limit_loose_interp,
                     edgecolor='k',
                     linewidth=0,
                     facecolor='k',
                     alpha=0.05)

    plt.text(float(data_loose['label_x']),
             float(data_loose['label_y']),
             data_loose['style']['label'],
             horizontalalignment='center',
             verticalalignment='top')


fig,ax = plt.subplots()
ax.set_yscale('log')
ax.set_xscale('log')

limits = yaml.load(open('../data/macho_limits.yaml'))

# plot_limit('gammaray_background_loose_carr_2016')
# plot_limit('gammaray_background_tight_carr_2016')
# plot_limit('gammaray_femtolens_carr_2016')
# plot_limit('ns_capture_loose_capela_2013')
# plot_limit('ns_capture_tight_capela_2013')
# plot_limit('kepler_griest_2013')
# plot_limit('hsc_niikura_2017')
# plot_limit('eros_tisserand_2007')
# plot_limit('macho_alcock_2001')
# plot_limit('eridanus_li_2016')
# plot_limit('eridanus_brandt_2016_tight')
# plot_limit('eridanus_brandt_2016_loose')

# plot_limit('lensed_sn_zumalacarregui_2018_tight')
# plot_limit('lensed_sn_garcia-bellido_2017_loose')

# plot_limit('binaries_quinn_2009_loose')
# plot_limit('binaries_yoo_2003_tight')

# plot_limit('disk_lacey_1985')

# plot_limit('plank_ali-haimoud_2016_loose')
# plot_limit('plank_ali-haimoud_2016_tight')
# plot_limit('cmb_ricotti_2008_tight')


plot_limit('lsst_m31_microlensing')
plot_limit('lsst_paralensing')
plot_limit('lsst_microlensing')

plot_two('gammaray_background_loose_carr_2016',
         'gammaray_background_tight_carr_2016')
plot_one('gammaray_femtolens_carr_2016')
plot_two('ns_capture_loose_capela_2013',
         'ns_capture_tight_capela_2013')
plot_one('hsc_niikura_2017')
plot_two('eridanus_brandt_2016_loose',
         'eridanus_brandt_2016_tight')
plot_two('lensed_sn_garcia-bellido_2017_loose',
         'lensed_sn_zumalacarregui_2018_tight')
plot_two('lensed_sn_garcia-bellido_2017_loose',
         'lensed_sn_zumalacarregui_2018_tight')
plot_one('eros_tisserand_2007')
plot_two('binaries_quinn_2009_loose',
         'binaries_yoo_2003_tight')
plot_two('plank_ali-haimoud_2016_loose',
         'cmb_ricotti_2008_tight')
plot_one('disk_lacey_1985')


plt.xlim(1e-18, 1e8)
plt.ylim(1e-5, 1.0)
plt.xlabel(r'${\rm Compact\ Object\ Mass}\ (M_\odot)$',fontsize=18)
plt.ylabel(r'${\rm Dark\ Matter\ Fraction}$', fontsize=18)
plt.subplots_adjust(top=0.95, bottom=0.12)


#plt.annotate(r'$\chi \chi \rightarrow b \bar b$', xy=(2e3,1e-27),fontsize=24)

plt.savefig('macho_limits.pdf')
plt.ion()

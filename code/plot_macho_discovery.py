#!/usr/bin/env python
"""
Plot projected PBH discovery histogram.

Adapted from Michael Medford.
"""
import pylab as plt
import numpy as np
import yaml
import copy
#from astropy.io import fits
import fitsio

import lsstplot
from lsstplot import COLORS

filename = lsstplot.get_datafile('pbh_popsycle_nocuts.fits')
data = fitsio.read(filename)

bins = np.log10(data['bin_edge'])
bin_width = np.unique(bins[1:] - bins[:-1])
bins = np.append(bins, bins[-1]+bin_width)
bins = 10**bins

scale = 10*10 / 3.74 # scaling 3.74 deg^2 to (10 x 10deg)

def plot_hist(x,y,**kwargs):
  defaults = dict(histtype='step',lw=2)
  label = kwargs.pop('label',None)
  n,b,p = plt.hist(x,weights=y,**kwargs)
  color = p[0].get_edgecolor()
  plt.plot(np.nan,np.nan,lw=kwargs['lw'],color=color,label=label)
  return n,b,p

plt.figure()
kwargs = dict(bins=bins,histtype='step',lw=2.5)

plot_hist(data['bin_edge'],scale*data['no_pbh'],label='No PBHs',
          color='k',zorder=10,**kwargs)
plot_hist(data['bin_edge'],scale*data['all_f 5'],label=r'$f_{PBH}=5\%$',
          color='skyblue',**kwargs)
plot_hist(data['bin_edge'],scale*data['all_f15'],label=r'$f_{PBH}=15\%$',
          color=COLORS['blue'],**kwargs)
plot_hist(data['bin_edge'],scale*data['all_f30'],label=r'$f_{PBH}=30\%$',
          color='b',**kwargs)

plt.gca().set_xscale('log'); plt.gca().set_yscale('log')
plt.xlim(1,6e3)

plt.legend(loc='upper right')

plt.xlabel(r'$t_E$ (days)',fontsize=18)
plt.ylabel('Number of Events',fontsize=18)

plt.savefig('macho_discovery.pdf',bbox_inches='tight')

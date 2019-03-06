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

np.random.seed(0)

def draw_hist(*args, **kwargs):
  kw = copy.deepcopy(kwargs)
  lw = kw.pop('lw',2)
  kw.update(histtype='stepfilled',lw=0)
  plt.hist(*args,**kw)
  kw.update(histtype='step',label=None,lw=lw)
  kw.pop('label',None)
  plt.hist(*args,**kw)

filename = "../data/OGLE_8_20_refined_events.fits"
data = fitsio.read(filename,columns=['rem_id_L','t_E','mass_L'])
data_BH = data[data['rem_id_L']==3]

#bins = np.logspace(np.log10(np.min(data['t_E'])),np.log10(np.max(data['t_E'])),26)
bins = np.logspace(-1,4,27)

fig,ax = plt.subplots()
kwargs = dict(lw=3,histtype='stepfilled',log=True,bins=bins)

draw_hist(data['t_E'],color='0.5',label=r'All Events',zorder=2,**kwargs)
draw_hist(data_BH['t_E'],color=COLORS['red'],label=r'Astrophysical BHs',zorder=3,alpha=0.3,**kwargs)

colors = ['green',COLORS['blue'],COLORS['orange']]
fracs = [.05,.15,.30]

for i,(color,frac) in enumerate(zip(colors,fracs)):
  N = int(len(data_BH)*frac)
  data_frac = copy.deepcopy(data)

  idx = np.random.choice(np.squeeze(np.where(data['rem_id_L']==3)),N,replace=False)
  #data_frac['t_E'][idx] *= np.sqrt(data_frac['mass_L'][idx]*10)
  data_frac['t_E'][idx] *= np.sqrt(10)

  draw_hist(data_frac['t_E'],color=color,label=r'All Events + %d\%% PBHs'%(frac*100),zorder=1-0.1*i,alpha=0.3,**kwargs)
  del data_frac

ax.legend(fontsize=14)
ax.set_xscale('log')
ax.set_xlim(1e-1, 1e4)
ax.set_xlabel(r'Einstein Crossing Time (days)',fontsize=20)
ax.set_ylabel('Number of Events',fontsize=20)
ax.xaxis.set_tick_params(labelsize=18)
ax.yaxis.set_tick_params(labelsize=18)

ax.set_axisbelow(True)
ax.grid(linestyle=':', linewidth=0.5, color='k', which='major', alpha=0.6)

fig.savefig('macho_discovery.pdf')

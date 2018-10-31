#!/usr/bin/env python
"""
Plot dark matter mass vs indirect detection decay lifetime.
"""
import pylab as plt
import numpy as np
import yaml
from StringIO import StringIO

def plot_gg_limit(section):
    data = limits[section]
    mass,limit = np.genfromtxt(StringIO(data['xystring'])).T
    kwargs = dict(**data['style'])
    plt.plot(mass,limit/2.,**kwargs)

def plot_gn_limit(section):
    data = limits[section]
    mass,limit = np.genfromtxt(StringIO(data['xystring'])).T
    kwargs = dict(**data['style'])
    #plt.plot(np.log10(mass),np.log10(limit),**kwargs)
    plt.plot(mass,limit,**kwargs)

fig,ax = plt.subplots()
ax.set_yscale('log')
ax.set_xscale('log')

limits = yaml.load(open('data/decay_limits.yaml'))

plot_gg_limit('heao-1')
plot_gg_limit('integral')
plot_gg_limit('comptel')
plot_gg_limit('egret')
plot_gn_limit('fermi')
#plot_limit('fermi_low')

plt.annotate(r'$\chi \rightarrow \gamma \nu$', xy=(3e1,1e26),fontsize=24)

plt.legend(loc='upper left')


plt.xlim(1e-6,1e3)
plt.ylim(5e25,5e30)
plt.xlabel(r'$m_{\rm DM}$ (GeV)',fontsize=18)
plt.ylabel('Decay Lifetime (s)',fontsize=18)
plt.subplots_adjust(top=0.95,bottom=0.12)


plt.savefig('id_decay.pdf')
plt.ion()

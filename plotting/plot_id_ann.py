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
    kwargs = dict(**data['style'])
    #plt.plot(np.log10(mass),np.log10(limit),**kwargs)
    plt.plot(mass,limit,**kwargs)

def plot_projection():
    data = limits['ackermann15_bb']
    mass,limit = np.genfromtxt(StringIO(data['xystring'])).T
    # Now for the projection factors
    proj_factor = np.ones(len(limit))

    # 1) apace predicts that the integrated J-factor could increase by a factor of 10
    proj_factor *= 10
    # 2) We expect to have ~18 years of data
    proj_factor *= 3
    # 3) the limits will scale as N^(1/2) at low mass and N^(1) at high mass
    # We fit to the curve in Fig 16 in 1605.02016
    slope = (0.5 - 0.75)/ (np.log10(6) - np.log10(1e4))
    fn = lambda mass: slope * np.log10(mass) + 0.43

    proj_factor = proj_factor**(-fn(mass))
    proj = proj_factor * limit

    kwargs=dict(ls='-',lw=1.5,color='dodgerblue')
    plt.plot(mass, proj, **kwargs)

fig,ax = plt.subplots()
ax.set_yscale('log')
ax.set_xscale('log')
plt.axhline(3e-26,ls='--',lw=2,color='gray')

limits = yaml.load(open('data/ann_limits.yaml'))

plot_limit('ackermann15_bb')
#plot_limit('gordon2013_bb_1s')
#plot_limit('abazajian2014_contour_bb_1s')
#plot_limit('calore2014_bb_1s')
#plot_limit('daylan2014_bb_1s')
plot_limit('hess_gc_einasto_abazajian_bb_95cl')
plot_limit('zaharijas2018_cta_bb')
plot_limit('gc_summary_bb_1s')

plot_projection()

plt.xlim(1,1e4)
plt.ylim(5e-28,1e-22)
plt.xlabel(r'$m_{\rm DM}$ (GeV)',fontsize=18)
plt.ylabel(r'$\langle \sigma_{\rm ann} v \rangle {\rm (cm^3 s^{-1})}$',fontsize=18)
plt.subplots_adjust(top=0.95,bottom=0.12)

plt.annotate(r'$\chi \chi \rightarrow b \bar b$', xy=(2e3,1e-27),fontsize=24)

plt.savefig('id_annih.pdf')
plt.ion()

#ell= Ellipse((1.6,-25.45), 0.37, 0.88)
#print(10**ell.get_patch_transform().transform(ell.get_path().vertices))

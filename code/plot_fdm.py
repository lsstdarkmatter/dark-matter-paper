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

def m22_nu(m22):
    return 1e-6 * (m22/40)

def nu_m22(nu):
    return  40 * nu / 1e-6

limits = yaml.load(open('data/fdm_limits.yaml'))

xticks=nu_m22(np.array([1e-6,1e-3,1,1e3,1e6]))*1e-22
xticklabels=[r'$\mu$Hz',r'mHz',r'Hz',r'kHz',r'MHz']
#xticklabels=[r'$10^{-6}$',r'$10^{-3}$',r'$1$',r'$10^{3}$',r'$10^{6}$']

fig,ax = plt.subplots()
ax.set_yscale('log')
ax.set_xscale('log')
ax2 = ax.twiny()

plot_limit(limits['coleman2018_magis100'])
plot_limit_fill(limits['graham2016_EP'])
plot_limit_fill(limits['schutz2020_streams'])

plot_lsst_limit(limits['lsst_dwarfs'])

ax2.set_xscale('log')
ax2.set_xticks(xticks)
ax2.set_xticklabels(xticklabels)

ax2.set_xlim(1e-22,1e-8)
ax.set_xlim(1e-22,1e-8)
ax.set_ylim(1e-32,1e-20)
ax.set_xlabel(r'Dark Matter Mass (eV)',fontsize=18)
ax.set_ylabel(r'Dark Matter Vector Coupling ($g_{B-L}$)',fontsize=18)

plt.subplots_adjust(top=0.90,bottom=0.12)

plt.savefig('fdm_limits_gBL.pdf')
plt.savefig('fdm_limits_gBL.png')
plt.ion()


fig,ax = plt.subplots()
ax.set_yscale('log')
ax.set_xscale('log')
ax2 = ax.twiny()

plot_limit_fill(limits['graham2013_sn1987a'])
plot_limit_fill(limits['wu2019_CASPEr_ZULF_Sideband'])
plot_limit_fill(limits['wu2019_CASPEr_ZULF_Comagnetometer'])
plot_limit_fill(limits['abel2017_neutrons_hg'])

x = copy.deepcopy(limits['schutz2020_streams'])
x['label_y'] = 1e-9
plot_limit_fill(x)

x = copy.deepcopy(limits['lsst_dwarfs'])
x['label_y'] = 1e-9
plot_lsst_limit(x)

ax2.set_xscale('log')
ax2.set_xticks(xticks)
ax2.set_xticklabels(xticklabels)

ax2.set_xlim(1e-22,1e-13)
ax.set_xlim(1e-22,1e-13)
ax.set_ylim(1e-12,1e-2)
ax.set_xlabel(r'Dark Matter Mass (eV)',fontsize=18)
ax.set_ylabel(r'$g_{aNN}\ ({\rm GeV^{-1}})$',fontsize=18)

plt.subplots_adjust(top=0.90,bottom=0.12)

plt.savefig('fdm_limits_gaNN.pdf')
plt.savefig('fdm_limits_gaNN.png')
plt.ion()


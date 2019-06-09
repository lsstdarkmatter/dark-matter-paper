#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 19:27:56 2019

@author: Francis-Yan Cyr-Racine, Harvard University
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from getdist import plots, loadMCSamples


# Generic properties from matplotlib
rcParams['font.family'] = 'serif'
rcParams['text.usetex'] = True

path_to_chains = '../data/'
chain_file = ['Post_FM_MWP_WDMP_data3_MWdwarfs']
labels = [r'LSST MW Sats. + Spec.']

samplesMC = []
# Load samples
for cfile in chain_file:
    samplesMC.append(loadMCSamples(path_to_chains + cfile + '/' + cfile))

g = plots.getSinglePlotter()
g.settings.figure_legend_frame = True
g.settings.tight_layout = True
g.settings.legend_fontsize = 16
g.settings.lab_fontsize = 20
g.plot_2d(samplesMC,['m_WDM','log_sigma_o_m'], filled=True,legend_loc='lower left', 
    line_args=[{'lw':1.5, 'color':'tab:blue'},
               {'lw':1.5,'color':'#85C1E9','ls':'--'}], 
    contour_colors=['tab:blue','#85C1E9'])
g.add_legend(labels,legend_loc='lower left')

ax  = plt.gca()
ax.set_xlim(2,20)
ax.set_xticks([2,4,6,8,10,12,14,16,18,20])
ax.set_ylabel(r'$\sigma_{\rm SIDM}/m_\chi\,({\rm cm}^2{\rm g}^{-1})$')

ax.set_ylim(-2,1)
ax.set_yticks([-2,-1,0,1])
ax.set_yticklabels([r'$10^{-2}$',r'$10^{-1}$',r'$10^0$',r'$10^1$'])

ax_c = ax.twiny()
ax_c.set_xlim(2,20)
ax_c.set_xticks([4,8,12,16,20])
ax_c.set_xticklabels([r'$1.6\times10^8$',r'$1.6\times10^7$',r'$4.1\times10^6$',r'$1.5\times10^6$',r'$7.4\times10^5$'],fontdict = {'fontsize':15})
ax_c.set_xlabel(r'$M_{\rm hm}\, (M_\odot)$',size = 20)

ax.scatter(6,np.log10(2),marker='*',c='r',s=60)

g.export('../figures/WDM_SIDM_discovery_test.pdf')

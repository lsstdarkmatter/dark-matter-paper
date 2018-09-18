#!/usr/bin/env python
"""
Plot dark matter mass vs indirect detection annihilation cross section.
"""
import pylab as plt
import numpy as np

fig,ax = plt.subplots()
ax.set_yscale('log')
ax.set_xscale('log')

plt.axhline(3e-26,ls='--',lw=2,color='gray')

plt.xlim(1,1e4)
plt.ylim(1e-27,1e-22)
plt.xlabel(r'$m_{\rm DM}$ (GeV)')
plt.ylabel(r'$\langle \sigma_{\rm SIDM} \rangle {\rm (cm^3 s^{-1})}$')

plt.savefig('id_annih.pdf')

#!/usr/bin/env python
"""
Plot dark matter mass vs indirect detection decay lifetime.
"""
import pylab as plt
import numpy as np

fig,ax = plt.subplots()
ax.set_yscale('log')
ax.set_xscale('log')

plt.axhline(3e-26,ls='--',lw=2,color='gray')

plt.xlim(1e-2,1e4)
plt.ylim(5e25,5e27)
plt.xlabel(r'$m_{\rm DM}$ (MeV)')
plt.ylabel(r'$\tau$ (s)')

plt.savefig('id_decay.pdf')

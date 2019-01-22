#!/usr/bin/env python
"""
Plot warm dark matter mass vs self-interaction scattering cross section.
"""
import pylab as plt
import numpy as np
from matplotlib.ticker import MaxNLocator, LogLocator
import matplotlib
matplotlib.rcParams['text.usetex'] = True

def latex_float(f):
    # https://stackoverflow.com/a/13490601
    float_str = "{0:.2g}".format(f)
    if "e" in float_str:
        base, exponent = float_str.split("e")
        return r"${0} \times 10^{{{1}}}$".format(base, int(exponent))
    else:
        return r"$%s$"%(float_str)

def mwdm2mhalo(mwdm):
    """
    Convert from warm dark matter particle mass to halo mass
    From Bullock & Boylan-Kolchin 2017

    Parameters:
    -----------
    mwdm : warm dark matter particle mass (keV)

    Returns:
    --------
    mhalo : halo mass (Msun)
    """
    return 5.5e10*(np.asarray(mwdm)/1.0)**-3.33

def mhalo2mwdm(mhalo):
    """
    Convert from halo mass to warm dark matter particle mass
    From Bullock & Boylan-Kolchin 2017

    Parameters:
    -----------
    mhalo : halo mass (Msun)

    Returns:
    --------
    mwdm : warm dark matter particle mass (keV)
    """
    return (np.asarray(mhalo)/5.5e10)**(1/-3.33)

fig,ax = plt.subplots()
ax2 = ax.twiny()
plt.sca(ax)

ax.set_yscale('log')
ax.set_xscale('linear')
ax2.set_xscale('linear')

##########################################
# Plot the data

plt.axvline(5.3,dashes=(5,2),lw=0.5,color='k')
plt.axvline(8.0,dashes=(5,2),lw=0.5,color='k')
plt.axvline(25.,dashes=(5,2),lw=0.5,color='k')

# This is just an example for illustration...
data = np.array([
    [0, 1e-2, 1e1],
    [1, 1e-2, 1e1],
    [5, 1e-2, 1e1],
    [7.672, 1e-2, 1e1],
    [7.672, 0.05929, 2.57658],
    [9.7198, 0.06186, 2.31756],
    [12.9567, 0.0631, 2.31756],
    [25, 0.0631, 2.317],
    [30,  0.0631, 2.317],
]).T

mass   = data[0]
bottom = data[1]
top    = data[2]

plt.fill_between(mass, bottom, y2=top,
                 edgecolor='tab:blue',
                 facecolor='tab:blue',
                 alpha=0.3)
plt.plot(mass,bottom,'-k',lw=1)
plt.plot(mass,top,'--k',lw=1)

mass = np.linspace(0,25,100)
plt.fill_between(mass, y1=1e-2, y2=1e1,
                 edgecolor='tab:gray',
                 facecolor='tab:gray',
                 alpha=0.3)

data = np.array([
   [ 2.71754, 0.010000  ],
   [ 2.71754, 0.107319  ],
   [ 3.24601, 0.182279  ],
   [ 4.10478, 0.296751  ],
   [ 4.63326, 0.374645  ],
   [ 5.02961, 0.443853  ],
   [ 5.29385, 0.49346   ],
   [ 5.49203, 0.525846  ],
   [ 5.55809, 0.572359  ],
   [ 5.62415, 0.609924  ],
   [ 5.62415, 0.678092  ],
   [ 5.55809, 0.770022  ],
   [ 5.16173, 0.931805  ],
   [ 4.5672 , 1.28045   ],
   [ 3.84055, 1.91518   ],
   [ 3.31207, 2.80448   ],
   [ 2.98178, 3.8538    ],
   [ 2.71754, 4.56572   ],
   [ 2.71754, 10        ],
]).T

xval = data[0]
yval = data[1]
plt.fill_betweenx(yval, x1=0,x2=xval,
                 edgecolor='black',
                 facecolor='red'
              )

##########################################

plt.xlim(0.5,30)
plt.ylim(0.01,10)

mhalo_ticks = np.array([ 2.6e8, 2.6e7, 6.7e6, 2.5e6, 1.2e6, 6.6e5 ])
ticklabels = [latex_float(x) for x in mhalo_ticks]

xticks = mhalo2mwdm(mhalo_ticks)
ax2.set_xlim(ax.get_xlim())
ax2.set_xticks(xticks)
ax2.set_xticklabels(ticklabels)

plt.xlabel(r'$m_{\rm WDM}\ {\rm (keV)}$',fontsize=20)
plt.ylabel(r'$\sigma_{\rm SIDM}/m_\chi\ {\rm (cm^2 g^{-1})}$',fontsize=20)
ax2.set_xlabel(r'${\rm M_{hm}\ (M_\odot)}$',fontsize=20)

plt.annotate(r'Probed by LSST Sats. + Spec',(17,0.4),ha='center',va='center')
plt.annotate(r'Probed by LSST Streams',(17,0.025),ha='center',va='center',)
plt.annotate(r'Probed by LSST Streams',(17,5.0),ha='center',va='center',)

plt.annotate(r'Approx. sensitivity of MW Sats. w/core collapse',(17,2.7),
             ha='center',va='center',fontsize=10)

plt.annotate(r'Excluded by Classical + SDSS MW Sats.',(1.5,0.3),ha='center',va='center',
             rotation=90.)

plt.annotate(r'Lyman-$\alpha$ (95\% CL)',(4.7,0.05),ha='center',va='center',
             rotation=90.,fontsize=10)
plt.annotate(r'Substructure Lensing (100 lenses)',(7.5,0.4),ha='center',va='center',
             rotation=90.,fontsize=10)

plt.savefig('wdm_sidm.pdf')


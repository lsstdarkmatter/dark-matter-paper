'''
'' Code to create a figure for the LSST DM book, on the uncertainty in the Mstar-Mhalo relation.
'' Annika Peter 10/30/18
'''

from numpy import *
from matplotlib import pyplot as plt

#--------------------------------------------------------------#
#                                                              #
# Define some Mstar-Mhalo relations from the literature        #
#                                                              #
#--------------------------------------------------------------#

def Mstar_Mhalo_Moster( massh, z ):
    ''' Moster et al. stellar mass--halo mass relation.  Benchmark model.
    ''  http://adsabs.harvard.edu/abs/2013MNRAS.428.3121M
    '''

    logM1z = 11.590 + 1.195*z/(1.+z)
    Nz = 0.0351 - 0.0247*z/(1.+z)
    betaz = 1.376 - 0.826*z/(1.+z)
    gammaz = 0.608 + 0.329*z/(1.+z)

    M1z = 10**logM1z

    return 2.*Nz*massh * ( (massh/M1z)**(-betaz) + (massh/M1z)**gammaz )**(-1.)


def Mstar_Mhalo_Read_Upper( massh ):
    ''' Mstar-Mhalo relation inferred by Read et al. 2017 
    ''
    '''
    return 0

#---------------------------------------------------------#
# Bookkeeping for masses and luminosities                 #
# The double-axis code is taken from                      #
# https://matplotlib.org/gallery/subplots_axes_and_figures/fahrenheit_celsius_scales.html#sphx-glr-gallery-subplots-axes-and-figures-fahrenheit-celsius-scales-py #
#---------------------------------------------------------#

def MV_from_Mstar( mstar, y=2 ):
    ''' Converts stellar mass to an absolute V band mag assuming a mass-to-light
    ''  ratio of y.  Default y is 2.  Assume Johnson V.  
    ''  Stellar mass should be in solar masses.
    '''
    MVSun = 4.81

    return MVSun - 2.5*log10( mstar/y )

def convert_ax_mstar_to_ax_abs( axmstar ):
    y1, y2 = axmstar.get_ylim()
    axabs.set_ylim( MV_from_Mstar(y1,y=2), MV_from_Mstar(y2,y=2))
    axabs.figure.canvas.draw()

mh = arange( 7, 15, 0.1 )
mh = 10**mh
mstarm = Mstar_Mhalo_Moster( mh, 0. )
mv = MV_from_Mstar( mstarm, y=2)

''' Convert right axis to absolute mag
'''
fig, axmstar = plt.subplots()

axabs = axmstar.twinx()

plt.figure(1)
axmstar.set_xlim(1e7,1e15)
axmstar.loglog(mh,mstarm)
axmstar.set_xlabel(r'$M_{halo} [M_{200c}$ in $M_\odot]$ central or infall')
axmstar.set_ylabel(r'$M_* [M_\odot]$')
axabs.semilogx(mh, mv )
y1, y2 = axmstar.get_ylim()
axabs.set_ylim( MV_from_Mstar( y1, y=2), MV_from_Mstar(y2,y=2 ))
axabs.set_ylabel(r'M$_V$')
plt.show()


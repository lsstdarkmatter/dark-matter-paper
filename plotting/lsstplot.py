#!/usr/bin/env python
"""
Generic python script.
"""
__author__ = "Alex Drlica-Wagner"

from StringIO import StringIO
import numpy as np
import pylab as plt
import matplotlib

from matplotlib.patches import Ellipse, PathPatch
from matplotlib.path import Path
matplotlib.rcParams['text.usetex'] = True

def get_mass_limit(data):
    mass,limit = np.genfromtxt(StringIO(data['xystring'])).T
    if data.get('mass_unit') == 'gram':
        mass /= 2e33
    elif data.get('mass_unit') == 'tev':
         mass *= 1e3
    return mass, limit

def plot_text(data):
    plt.text(float(data['label_x']),
             float(data['label_y']),
             data['style']['label'],
             horizontalalignment='center',
             verticalalignment='top')

def plot_limit(data):
    mass,limit = get_mass_limit(data)
    kwargs = dict(**data['style'])
    plt.plot(mass, limit, **kwargs)
    plot_text(data)

def plot_limit_fill(data, low=False):
    mass,limit = get_mass_limit(data)

    kwargs = dict(**data['style'])
    kwargs.setdefault('lw', 2)
    kwargs.setdefault('alpha', 0.3)

    plt.fill_between(mass, limit, y2 = 1 if not low else 0,
                     edgecolor='tab:%s'%kwargs['color'],
                     facecolor='tab:%s'%kwargs['color'],
                     alpha=kwargs['alpha'])
    plot_text(data)

def plot_limit_patch(data):
    mass,limit = get_mass_limit(data)
    kwargs = dict(**data['style'])
    kwargs.setdefault('lw',2)
    kwargs.setdefault('alpha',0.3)

    patch = PathPatch(Path(zip(mass, limit)),
                      edgecolor='tab:%s'%kwargs['color'],
                      facecolor='tab:%s'%kwargs['color'],
                     alpha=kwargs['alpha'])
    plt.gca().add_artist(patch)
    plot_text(data)

def plot_one(data):
    mass,limit = get_mass_limit(data)

    kwargs = dict(**data['style'])
    plt.fill_between(mass, limit, y2=1.0,
                     edgecolor='tab:blue',
                     facecolor='tab:blue',
                     alpha=0.3)
    plot_text(data)

def plot_two(data_loose, data_tight):
    mass_loose,limit_loose = get_mass_limit(data_loose)
    mass_tight,limit_tight = get_mass_limit(data_tight)

    # Interpolate the data to a common grid
    x_min = np.min((np.min(mass_loose), np.min(mass_tight)))
    x_max = np.max((np.max(mass_loose), np.max(mass_tight)))
    x = np.logspace(np.log10(x_min), np.log10(x_max), num=100)
    limit_loose_interp = np.interp(x, mass_loose, limit_loose)
    limit_tight_interp = np.interp(x, mass_tight, limit_tight)

    plt.fill_between(mass_loose, limit_loose, y2=1.0,
                     edgecolor='tab:blue',
                     facecolor='tab:blue',
                     alpha=0.3)
    plt.fill_between(x, limit_tight_interp, limit_loose_interp,
                     edgecolor='k',
                     linewidth=0,
                     facecolor='k',
                     alpha=0.05)
    plot_text(data_loose)

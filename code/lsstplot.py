#!/usr/bin/env python
"""
Generic python script.
"""
__author__ = "Alex Drlica-Wagner"
import os
from StringIO import StringIO
from collections import OrderedDict as odict
import numpy as np
import pylab as plt
import matplotlib

from matplotlib.patches import Ellipse, PathPatch
from matplotlib.path import Path
matplotlib.rcParams['text.usetex'] = True

COLORS = odict([
    ('blue','#1F77B4'),  # This is original T10 "tab:blue"
    ('gray','#7F7F7F'),  # This is original T10 "tab:gray"
    ('orange','orange'),
    ('gold','orange'),
    ('red','#FA0303'),   # T10 color is #D62728
    ('black','k'),   # T10 color is #D62728
])
ALPHA = 0.35
LINEWIDTH = 2

DEFAULTS = dict(color=COLORS['blue'],alpha=ALPHA,linewidth=LINEWIDTH)

def get_datadir():
    """Get the data directory. Could live here or up one level."""
    if os.path.exists('./data'):
        return './data'
    elif os.path.exists('../data'):
        return '../data'
    else:
        raise IOError("Data directory not found.")

def get_datafile(filename):
    """Get a data file."""
    datadir = get_datadir()
    path = os.path.join(datadir,filename)
    if not os.path.exists(path):
        raise IOError("Data file not found: %s"%path)
    return path

def setdefaults(kwargs,defaults):
    for k,v in defaults.items():
        kwargs.setdefault(k,v)
    return kwargs

def get_mass_limit(data):
    mass,limit = np.genfromtxt(StringIO(data['xystring'])).T
    if data.get('mass_unit') == 'gram':
        mass /= 2e33
    elif data.get('mass_unit') == 'tev':
         mass *= 1e3
    return mass, limit

def plot_text(data,**kwargs):
    kw = dict(ha='center',  va='top', rotation=data.get('rotation',0))
    kw.update(kwargs)
    return plt.text(float(data['label_x']),
                    float(data['label_y']),
                    data['style']['label'],
                    **kw
                    )

def plot_limit(data, **kwargs):
    mass,limit = get_mass_limit(data)
    kw = dict(**data['style'])
    kw.update(kwargs)
    plt.plot(mass, limit, **kw)
    plot_text(data)

def plot_limit_fill(data, low=False, **kwargs):
    mass,limit = get_mass_limit(data)

    kw = dict(**data['style'])
    kw.update(**kwargs)
    setdefaults(kw,DEFAULTS)

    plt.fill_between(mass, limit, y2 = 1 if not low else 0,
                     edgecolor=kw['color'],
                     facecolor=kw['color'],
                     alpha=kw['alpha'],
    )
    plot_text(data)


def plot_lsst_limit(data, low=False, **kwargs):
    kw = dict(**data['style'])
    kw.update(kwargs)
    setdefaults(kw,{'alpha':0.15})
    setdefaults(kwargs,DEFAULTS)

    mass,limit = get_mass_limit(data)
    plt.fill_between(mass, limit, y2 = 1 if not low else 0,
                     edgecolor=kw['color'],
                     facecolor=kw['color'],
                     #facecolor='none', hatch = '/',
                     alpha=kw['alpha'],
    )
    plot_text(data)

    kw['alpha'] = 1
    plt.plot(mass, limit, **kw)


def plot_limit_patch(data,**kwargs):
    kw = dict(**data['style'])
    kw.update(kwargs)
    setdefaults(kw,DEFAULTS)

    mass,limit = get_mass_limit(data)
    patch = PathPatch(Path(zip(mass, limit)),
                      edgecolor=kw['color'],
                      facecolor=kw['color'],
                     alpha=kw['alpha'])
    plt.gca().add_artist(patch)
    plot_text(data)

def plot_one(data,**kwargs):
    kw = dict(**data['style'])
    kw.update(kwargs)
    setdefaults(kw,DEFAULTS)

    mass,limit = get_mass_limit(data)
    plt.fill_between(mass, limit, y2=1.0,
                     edgecolor=COLORS['blue'],
                     facecolor=COLORS['blue'],
                     alpha=kw['alpha'])
    plot_text(data)

def plot_two(data_loose, data_tight, **kwargs):
    kw = dict(**data_loose['style'])
    kw.update(**kwargs)
    setdefaults(kw,DEFAULTS)

    mass_loose,limit_loose = get_mass_limit(data_loose)
    mass_tight,limit_tight = get_mass_limit(data_tight)

    # Interpolate the data to a common grid
    x_min = np.min((np.min(mass_loose), np.min(mass_tight)))
    x_max = np.max((np.max(mass_loose), np.max(mass_tight)))
    x = np.logspace(np.log10(x_min), np.log10(x_max), num=100)
    limit_loose_interp = np.interp(x, mass_loose, limit_loose)
    limit_tight_interp = np.interp(x, mass_tight, limit_tight)

    plt.fill_between(mass_loose, limit_loose, y2=1.0,
                     edgecolor=COLORS['blue'],
                     facecolor=COLORS['blue'],
                     alpha=kw['alpha'])
    plt.fill_between(x, limit_tight_interp, limit_loose_interp,
                     edgecolor='k',
                     linewidth=0,
                     facecolor='k',
                     alpha=0.07)
    plot_text(data_loose)

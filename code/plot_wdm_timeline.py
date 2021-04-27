#!/usr/bin/env python
"""
Generic python script.
"""
__author__ = "Alex Drlica-Wagner"
import pylab as plt
import numpy as np
from dateutil.parser import parse
from collections import OrderedDict as odict
import yaml

LIMITS = yaml.safe_load(open('data/wdm_timeline.yaml'))

COLORS=odict([
    ('lya',(r'Lyman-$\alpha$','tab:blue')),
    ('dsphs',(r'MW Satellites','tab:green')),
    ('grav imaging',(r'Grav. Imaging','tab:orange')),
    ('flux ratios',(r'Flux Ratios','tab:red')),
    #('streams','black'),
    ('combo',(r'Combinations','tab:purple')),
])

fig,ax = plt.subplots()
kwargs=dict(lolims=True,lw=3,capsize=8,capthick=3)
for key,val in LIMITS.items():
    if val['type'] == 'streams': continue
    print(key)
    label,color=COLORS[val['type']]
    date = parse(val['date'])
    if len(val['mwdm']) == 1:
        plt.errorbar(date,val['mwdm'][0],yerr=1.0,
                     color=color,**kwargs)
    else:
        fudge = 0.5 # fudge factor for cap height
        y = plt.errorbar(date,val['mwdm'][0],
                         yerr=val['mwdm'][1]-val['mwdm'][0] - fudge,
                         color=color,**kwargs)
        #y[1][0].set_marker('_')
        #plt.setp(y[-1],capstyle="round")
        x = plt.errorbar(date,val['mwdm'][1],
                         yerr=1.0,
                         color=color,ls='--',**kwargs)
        x[-1][0].set_linestyle('--')

    #plt.annotate(key,(date,val['mwdm'][0]-0.5),fontsize=10,ha='center')

for key,val in COLORS.items():
    plt.plot(np.nan,np.nan,lw=3,color=val[1],label=val[0])

plt.ylim(-0.5,13)
plt.grid(ls=':')
plt.legend(loc='upper left')
plt.xlabel("Publication Year",fontsize=18)
plt.ylabel("Constraint on WDM Mass (keV)",fontsize=18)
plt.show()

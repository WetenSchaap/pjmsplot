#%% Testing...
# see if I did this packaging thing correctly.

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
import matplotlib.pyplot as plt
import pjmsplot

def simpleplot():
    fig,ax = plt.subplots(1,1)
    x = np.linspace(0,2*np.pi,100)
    y = np.sin(x)
    ax.plot(
        x,
        y,
    )
    return fig,ax

#%% load package and see if plotting works

import pjmsplot as pp

fig,ax = simpleplot()
pp.squarify(fig)

#%% Compare to direct setting of values to see if it worked

import matplotlib as mpl
import matplotlib.pyplot as plt
############################
#% PLOT SETTINGS
############################
# FONT SIZES:
SMALL_SIZE = 10
MEDIUM_SIZE = 15
BIGGER_SIZE = 20

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)   # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)   # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)   # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

# LINE PROPERTIES:
plt.rc('lines', linewidth=4)             # marker size
plt.rc('lines', markersize=11)           # marker size
plt.rc('lines', markeredgewidth=0)       # marker edge width

# LINEWIDTH (OF EDGES):
LINEWIDTH = 2 #0.8 is default
plt.rc('axes', linewidth= LINEWIDTH)
mpl.rcParams['xtick.major.width'] = LINEWIDTH
mpl.rcParams['ytick.major.width'] = LINEWIDTH

# AUTOMATIC COLOR CYCLE # Disable --> has weird side effects.
# from cycler import cycler
# default_cycler = (cycler(color = ['red','blue','#dba800','green']) + 
#                 #   cycler(linestyle = ['-', '--', ':', '-.']) + 
#                   cycler(marker = ['o','s','D','h'])
# plt.rc('axes', prop_cycle= default_cycler)

# Figure quality (in case of jpg/png/...)
mpl.rcParams['figure.dpi'] = 300


fig,ax = simpleplot()
pp.squarify(fig)

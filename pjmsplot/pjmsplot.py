# -*- coding: utf-8 -*-
"""
pjmsplot
Originally created on 04/08/2021

@author: Piet

Stuff for making plotting easy and consistent.

Most important are:
    * Sets sane defaults for plot settings, like line thickness and ticklabelsize

    * squarify: function to make any plot square:
        >>> squarify(fig)
        [figure is now square]
    
    * Gives access to some small nice things, like extra line styles.
        >>> plt.plot(x,y,linestyle = linestyle_dict['loosely dashdotdotted'])

    * I would advise using tol-colors package to manage your colors.
"""

import matplotlib as mpl
import matplotlib.pyplot as plt

############################
#% FUNCTIONS
############################

def squarify(fig):
    """
    Make any matplotlib figure square!
    Just do all the setupe and end with:
        >>> squarify(fig)
    This should do the trick without worries.
    """
    w, h = fig.get_size_inches()
    if w > h:
        t = fig.subplotpars.top
        b = fig.subplotpars.bottom
        axs = h*(t-b)
        l = (1.-axs/w)/2
        fig.subplots_adjust(left=l, right=1-l)
    else:
        t = fig.subplotpars.right
        b = fig.subplotpars.left
        axs = w*(t-b)
        l = (1.-axs/h)/2
        fig.subplots_adjust(bottom=l, top=1-l)

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
dpi = 300
mpl.rcParams['figure.dpi'] = dpi
mpl.rcParams['savefig.dpi'] = dpi # not sure if needed but cannot be too carefull

# Bounding box size (tight is really the only sane option, why is this not always on?!)
mpl.rcParams['savefig.bbox'] = "tight"
mpl.rcParams['savefig.pad_inches'] = 0.1

############################
#% USEFULL SETTINGS
############################

# EXTRA LINESTYLES
linestyle_dict = {
    # defaults:
    'solid':                 'solid',      # Same as (0, ()) or '-'
    'dotted':                'dotted',    # Same as (0, (1, 1)) or '.'
    'dashed':                'dashed',    # Same as '--'
    'dashdot':               'dashdot',  # Same as '-.'
    
    'loosely dotted':        (0, (1, 10)),
    'dotted':                (0, (1, 1)),
    'densely dotted':        (0, (1, 1)),

    'loosely dashed':        (0, (5, 10)),
    'dashed':                (0, (5, 5)),
    'densely dashed':        (0, (5, 1)),

    'loosely dashdotted':    (0, (3, 10, 1, 10)),
    'dashdotted':            (0, (3, 5, 1, 5)),
    'densely dashdotted':    (0, (3, 1, 1, 1)),

    'dashdotdotted':         (0, (3, 5, 1, 5, 1, 5)),
    'loosely dashdotdotted': (0, (3, 10, 1, 10, 1, 10)),
    'densely dashdotdotted': (0, (3, 1, 1, 1, 1, 1))
}


############################
#% USEFULL TIPS
############################
## to get a specific color on a certain value in a color scale:
# cmap = mpl.cm.get_cmap('viridis')
# rgba = cmap(0.5)
# print(rgba) # (0.127568, 0.566949, 0.550556, 1.0)
## Optionally, normalize: 
# norm = mpl.colors.Normalize(vmin=10.0, vmax=20.0)
# rgba = cmap(norm(15)) # norm results in 0.5
# print(rgba) # (0.127568, 0.566949, 0.550556, 1.0)
# see test below for clear example.


if __name__ == "__main__":
    """
    Quickly test plotting so you can see what a plot will look like. Running from the commandline will result in poorly squarified plots, so don't worry about that too much.
    """
    import numpy as np
    import tol_colors as tc
    # generate a bunch of discrete data and plot it
    datasets = 4
    # colors:
    cset = tc.tol_cset("light")
    x = np.linspace(0,10*np.pi,100)
    y = list()

    fig,ax = plt.subplots(1,1)

    for i in range(datasets):
        y.append( np.sin(x*(i+1)*0.1) )
        ax.plot(
            x,
            y[i],
            '-',
            color = cset[i],
            linewidth = 4
        )
    squarify(fig)
    plt.show()
    
    # generate a bunch of continueous data and plot it
    datasets = 10
    # colors:
    cset = tc.tol_cmap("iridescent")
    norm = mpl.colors.Normalize(vmin=0, vmax=datasets)
    x = np.linspace(0,10*np.pi,1000)
    y = list()

    fig,ax = plt.subplots(1,1)

    for i in range(datasets):
        y.append( np.sin(x*(i+1)*0.1) )
        rgba = cset(norm(i))
        ax.plot(
            x,
            y[i],
            '-',
            color = rgba,
            linewidth = 4
        )
    squarify(fig)
    plt.show()
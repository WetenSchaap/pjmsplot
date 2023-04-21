"""
Clearly, this test thing exists only for the idea. It is not so easy to test whether plots come out nice. At best you may expect an error during plotting. But things may still just look bad if that does not happen. At any rate, I guess it's good practice.
"""

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
import matplotlib.pyplot as plt
import pjmsplot
import pytest

def test_lsdict():
    """Check if this linestyle_dict exists"""
    assert pjmsplot.linestyle_dict["dashdot"] == "dashdot"

def simpleplot():
    fig,ax = plt.subplots(1,1)
    x = np.linspace(0,2*np.pi,100)
    y = np.sin(x)
    ax.plot(
        x,
        y,
    )
    return fig,ax

def test_plotting():
    f,a = simpleplot()
    assert f
    assert a

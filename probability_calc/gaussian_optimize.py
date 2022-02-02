#! /usr/bin/python

"""
Contains functions that adjust standard deviation and mean
of a gaussian distribution variable to minimize production loss

Version 1.0

Author: Billy Shi
Date: Feb 1, 2022
"""

import random
import numpy as np
from scipy.integrate import quad

def gaussian_optimize(mean, sd, bounds, x):
    """
    given the mean, standard deviation and boundaries,
    returns the probability of variable value outside bounds
    as well as the desired mean or standard deviation to minimize this probability

    :param mean: mean value of a gaussian distribution
    :type mean: float
    :param sd: standard deviation
    :type sd: float
    :param bounds: upper and/or lower bounds
    :type bounds: list
    :param x: sample space, default from -infty to +infty
    :type x: list
    """
    
    # calculate proportion outside bounds
    return gaussian_cumulative(0.01)

def gaussian_cumulative(z):
    """
    gaussian cumulative probability function
    """
    def f(x):
        return np.exp(-0.5 * x**2)
    res, err = quad(f, 1e-9, z)
    res = res/np.sqrt(2*np.pi) + 0.5
    err = err/np.sqrt(2*np.pi)
    return [res, err]

print(gaussian_cumulative(1)[0])
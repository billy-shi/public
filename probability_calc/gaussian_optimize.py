#! /usr/bin/python

"""
Contains functions that adjust standard deviation and mean
of a gaussian distribution variable to minimize production loss

Version 1.0

Author: Billy Shi
Date: Feb 1, 2022
"""

import numpy as np
from scipy.integrate import quad

def gaussian_reject(mean, sd, bounds):
    """
    given the mean, standard deviation and boundaries,
    returns the probability of variable value outside bounds

    :param mean: mean value of a gaussian distribution
    :type mean: float
    :param sd: standard deviation
    :type sd: float
    :param bounds: upper and/or lower bounds in format [upper, lower]
    :type bounds: list
    """
    
    # calculate z_score for upper rejection
    z_up = abs(bounds[0] - mean)/sd
    res = 1 - z_score(z_up)

    # calculate z_score for lower rejection
    if len(bounds) == 2:
        z_low = abs(bounds[1] - mean)/sd
    res += 1 - z_score(z_low)

    return res

def gaussian_optimize(bounds, sd):
    """
    given the bounds and standard deviation,
    return the lowest proportion rejected possible and the mean required

    :param bounds: upper and lower bounds in format [upper, lower]
    :type bounds: list
    :param sd: value of standard deviation
    :type reference: float
    """

    # checks
    if len(bounds) != 2:
        raise ValueError("2 elements inside bounds expected")

    mean = sum(bounds)/2
    rejected = 2 - z_score(abs(bounds[0]-mean)) - z_score(abs(bounds[1]-mean))

    return rejected, mean


def z_score(z):
    """
    gaussian cumulative probability function (z-score) table
    """
    def f(x):
        return np.exp(-0.5 * x**2)
    res, err = quad(f, 1e-9, z)
    res = res/np.sqrt(2*np.pi) + 0.5
    err = err/np.sqrt(2*np.pi)
    return [res, err]
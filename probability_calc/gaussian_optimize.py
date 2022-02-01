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
    gaussian(x)

def gaussian(x, mean, sd):
    """
    gaussian distribution function
    
    :param x: values to consider distributions
    :type x: list
    :param mean: mean value of a gaussian distribution
    :type mean: float
    :param sd: standard deviation
    :type sd: float
    """

    p_density = (np.pi*sd) * np.exp(-0.5*((x-mean)/sd)**2)
    return p_density

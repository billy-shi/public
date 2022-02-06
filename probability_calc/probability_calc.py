#! /usr/bin/python

"""
This programme solve a series of probability questions

Version 1.0

Author: Billy Shi
Date: Jan 22, 2022
"""

import random
import numpy
import matplotlib.pyplot as plt

from probability_calc import gaussian_optimize

class Probability:
    def __init__(self, mean, sd):
        self.mean = mean
        self.sd = sd

    def gaussian(self):
        
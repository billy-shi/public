#! /usr/bin/python

"""
By inputting a transfer function, program plots Bode and Nyquist plots of system
Program prints gain and phase margins

Version 1.0

Author: Billy Shi
Date: Dec 27, 2021
"""

import matplotlib.pyplot as plt
import control as ctr
import numpy as np

def plot():
    num_deg = input("How many terms are in numerator: ")
    assert num_deg.isdigit(), "You didn't enter a positive integer"
    num_comma = input("Separated by comma, enter numerator coefficients in descending order: ")
    num = num_comma.split(",")
    num = [int(n) for n in num]
    assert len(num) == int(num_deg), "Your entries contradict"

    dnom_deg = input("How many terms are in denominator: ")
    assert dnom_deg.isdigit(), "You didn't enter a positive integer"
    dnom_comma = input("Separated by comma, enter denominator coefficients in descending order: ")
    dnom = dnom_comma.split(",")
    dnom = [int(n) for n in dnom]
    assert len(dnom) == int(dnom_deg), "Your entries contradict"

    G = ctr.tf(num,dnom)
    print(G)
    fig1 = plt.figure()
    ctr.nyquist(G)
    plt.grid()
    fig2 = plt.figure()
    mag, phase, omega = ctr.bode(G,np.geomspace(0.1,1000,80))
    print("Gain margin of system is: " + str(ctr.margin(G)[0]))
    print("Phase margin of system is: " + str(ctr.margin(G)[1]) + " degrees")
    plt.show()

while True:
    print("Welcome!")
    print("We will plot Nyquist and Bode plots for you")
    print("Provided with a open-loop transfer function")
    try:
        plot()
    except:
        print("Oops, something went wrong. Please retry")
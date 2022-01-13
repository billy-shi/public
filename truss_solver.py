#! /usr/bin/python

"""
Solves indeterminate trusses - an interactive program

Version 1.0

Author: Billy Shi
Date: Jan 3, 2022
"""

import numpy as np

# step 1: num of bars and num of redundancy
bars_num = input("How many bars are there? ")
redun = input("How many redundancies? ")
try:
    redun = int(redun)
    bars_num = int(bars_num)
except:
    ValueError("Sorry, I can't process the value you provided")
assert redun > 0 and bars_num > 0 and redun < bars_num, "Sorry, values entered are invalid"

# Step 2: tension vectors
# load tension
t = [0]*bars_num
t_input = input("Separated by comma, enter loaded tensions assuming load is 1: ")
t_input = t_input.split(",")
t = [int(n) for n in t_input]
assert len(t) == bars_num, "Sorry, values entered are invalid"

# self stresses
s = [[0]*bars_num]*redun
for i in range(len(s)):
    if i == 0:
        s_input = input("Separated by comma, enter first self stress vector: ")
    else:
        s_input = input("Separated by comma, enter next self stress vector: ")
    s_input = s_input.split(",")
    s[i] = [int(n) for n in s_input]
    assert len(s[i]) == bars_num, "Sorry, values entered are invalid"

# flexibility matrix
l = [0]*bars_num
l_input = input("Separated by comma, enter lengths of bars assuming L = 1 as standard: ")
l_input = l_input.split(",")
l = [int(n) for n in l_input]
assert len(l) == bars_num, "Sorry, values entered are invalid"
F = np.diag(l)

# calculate extensions
load_e = F.dot(t)
print(load_e)
self_e = [0]*bars_num
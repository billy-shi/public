#! /usr/bin/python

"""
By inputting necessary information about an indeterminate truss, this program returns
the compatible extensions of a truss

Version 1.0

Author: Billy Shi
Date: Dec 29, 2021
"""

import numpy as np
import tkinter as tk
from tkinter import simpledialog

# generalize an error window
def error():
    root = tk.Tk()
    root.title("Sorry! Your inputs are not valid!")
    root.geometry('300x50')
    q_button = tk.Button(root, text='Try Again', command=root.quit)
    q_button.pack(side=tk.BOTTOM, padx=5, pady=5)
    root.mainloop()

# Step 1: obtain number of bars and redundancies
fields = 'Num of Bars', 'Num of Redundancies'
def window1(root, fields):
    entries1 = []
    for field in fields:
        row = tk.Frame(root)
        lab = tk.Label(row, width=15, text=field, anchor='w')
        ent = tk.Entry(row)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entries1.append((field, ent))
    return entries1
bar_num = 0
redun = 0
def fetch1(entries1):   # fetch data from entries
    global bar_num
    global redun
    bar_num = entries1[0][1].get()
    redun = entries1[1][1].get()

print("We are ready to solve your indeterminate truss")
print("Please calculate and enter values in the window")
root = tk.Tk()
root.title("Number of Bars and Redundancies")
ents = window1(root, fields)
s_button = tk.Button(root, text='Store', command=(lambda e=ents: fetch1(e)))
q_button = tk.Button(root, text='Next', command=root.quit)
s_button.pack(side=tk.LEFT, padx=5, pady=5)
q_button.pack(side=tk.LEFT, padx=5, pady=5)
root.mainloop()
if int(bar_num) <= 1 or int(redun) <= 0:
    error()
    quit()

# Step 2: ask for lengths of each bar
def window2(root, bar_num):
    entries2 = []
    for i in range(1, int(bar_num)+1):
        row = tk.Frame(root)
        text = "Bar" + str(i)
        lab = tk.Label(row, width=15, text=text, anchor='w')
        ent = tk.Entry(row)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entries2.append(ent)
    return entries2
bars_len = []
def fetch2(entries2):   # fetch entered bar lengths
    global bars_len
    bar_len = entries2

print("Thanks. We will now need more information")
root = tk.Tk()
root.title("Enter Lengths of Bars")
ents = window2(root, bar_num)
s_button = tk.Button(root, text='Store', command=(lambda e=ents: fetch2(e)))
q_button = tk.Button(root, text='Next', command=root.quit)
s_button.pack(side=tk.LEFT, padx=5, pady=5)
q_button.pack(side=tk.LEFT, padx=5, pady=5)
root.mainloop()
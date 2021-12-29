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
fields = 'Last Name', 'First Name', 'Job', 'Country'
def bars():
    window = tk.Tk()
    window.withdraw()
    bars = simpledialog.askstring(title="Number of Bars", prompt="How many bars are there?")
    assert int(bars)
    bars = int(bars)
    return bars

def fetch(entries):
    for entry in entries:
        field = entry[0]
        text  = entry[1].get()
        print('%s: "%s"' % (field, text)) 

def makeform(root, fields):
    entries = []
    for field in fields:
        row = tk.Frame(root)
        lab = tk.Label(row, width=15, text=field, anchor='w')
        ent = tk.Entry(row)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entries.append((field, ent))
    return entries

if True:
    print("We are ready to solve your indeterminate truss")
    print("Please calculate and enter values as prompted")
    root = tk.Tk()
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
    b1 = tk.Button(root, text='Show',
                  command=(lambda e=ents: fetch(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    b2 = tk.Button(root, text='Quit', command=root.quit)
    b2.pack(side=tk.LEFT, padx=5, pady=5)
    root.mainloop()




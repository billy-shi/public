#! /usr/bin/python

"""
By inputting a combination of numbers from 2-9, program returns all possibility
of string combinations that correspond to 9-key phone keyboard.

Version 1.0

Author: Billy Shi
Date: Jan 2, 2022
"""
from itertools import product

def PhoneNumCombine(digits):
        # create a dictionary
        num_dict = {"2":["a", "b", "c"], "3":["d", "e", "f"], "4":["g", "h", "i"],
                   "5":["j", "k", "l"], "6":["m", "n", "o"], "7":["p", "q", "r", "s"],
                   "8":["t", "u", "v"], "9":["w", "x", "y", "z"]}
        # cover corner cases 
        if "1" in digits or digits == "":
            return []
        if len(digits) == 1:
            return num_dict[digits]
        
        # get cartenian products
        if len(digits) == 2:
            prdts = product(num_dict[digits[0]], num_dict[digits[1]])
        elif len(digits) == 3:
            prdts = product(num_dict[digits[0]], num_dict[digits[1]], num_dict[digits[2]])
        elif len(digits) == 4:
            prdts = product(num_dict[digits[0]], num_dict[digits[1]], num_dict[digits[2]], num_dict[digits[3]])
        
        res = list(prdts)
        # remove commas
        for i in range(len(res)):
            res[i] = ''.join(res[i])
        
        return res

digits = "562"
ans = ["jma","jmb","jmc","jna","jnb","jnc","joa","job","joc","kma","kmb","kmc","kna","knb","knc","koa","kob","koc","lma","lmb","lmc","lna","lnb","lnc","loa","lob","loc"]
assert PhoneNumCombine(digits) == ans
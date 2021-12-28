#! /usr/bin/python

"""
This programme solves an online coding challenge of manupulating arrays based on prime numbers

Version 1.0

Author: Billy Shi
Date: Dec 24, 2021
"""

### Problem Statement (paraphased)
"""
One row of lights start with a current state, each can be turned on (1) or off (0). This is provided
in an array called /states/. Another integer is provided called /number/.
For this number, we change the state of the light that correspond to the multiples of its prime factors.

For example: if initial /states/ is [1, 1, 1, 1, 1, 1]
Number is 6 with prime factors 2 and 3
We change the states of lights 2, 4, 6 because they are multiples of 2
We then change states of lights 3, 6 because that is multiple of 3

For a more advanced version, the variable /numbers/ can contain an array of numbers.
Each number carries out the above steps.

Output the final states of lights in an array.
"""

### Solution Overview
"""
Approach this solution by breaking down steps:
1. For each number in /numbers/, get its prime factors
2. For each prime factor, work out the lights that need state change
3. Change light state and store it for next iteration
"""

import numpy as np

def PrimeLight(states, numbers):
    # function to obtain all prime factors
    def primefactor(n):
        res = []
        # if n is even
        while n % 2 == 0:
            if 2 not in res:
                res.append(2)
            n = n / 2
        # now n must be even
        for i in range(3,int(np.sqrt(n))+1,2):
            while n % i == 0:
                if i not in res:
                    res.append(i)
                n = n / i
        # finally include n itself
        if n > 2 and n not in res:
            res.append(int(n))
        return res
    # obtain prime factors for numbers
    for i in range(len(numbers)):
        numbers[i] = primefactor(numbers[i])
        temp = []
        for prime in numbers[i]:
            temp = temp + list(np.arange(prime, prime*(len(states)//prime)+1, prime))
        numbers[i] = temp
        # now the variable numbers contain lights needing state change
        for l in numbers[i]:
            if states[l-1] == 1:
                states[l-1] = 0
            elif states[l-1] == 0:
                states[l-1] = 1

    return states


# Run program
states = [1,1,0,0,1,1,0,1,1,1]
numbers = [3,4,15]
assert PrimeLight(states, numbers) == [1,0,0,1,0,0,0,0,1,1]
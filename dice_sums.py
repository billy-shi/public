#! /usr/bin/python

"""
A solution programme for an online coding challenge:
Two arrays A and B are given which correspond to numbers of N and M dices.
The program returns the minimum number of rerolls needed so that the two arrays
A and B have the same sum.

For example, A = [1, 2, 3, 4] and B = [5, 6], then minimum 1 reroll is needed
to change 6 to 5, so both A and B arrays sum to 10.

Version 1.0

Author: Billy Shi
Date: Jan 30, 2022
"""

import heapq

def dice_sums(A, B):
    # initialise variables
    diff = sum(A) - sum(B)
    if diff == 0:
        return 0  # same sum already
    elif diff < 0:
        big_sum, sml_sum = B, A
    else:
        big_sum, sml_sum = A, B
    diff = abs(diff)
    count = 0

    # create heaps
    heapq.heapify(sml_sum)
    big_sum = [-i for i in big_sum]
    heapq.heapify(big_sum) # -1 for popping later

    # take min from sml_sum and max from big_sum
    # sum their contribution towards equal sum
    while diff > 0:
        if sml_sum[0] == 6 and abs(big_sum[0]) == 1:
            return -1  # impossible equal sum
        
        sml_margin = 6 - sml_sum[0]
        big_margin = abs(big_sum[0]) - 1
        count += 1 # number of dices turned
        diff -= max(sml_margin, big_margin)  

        if sml_margin > big_margin:
            # min from sml_sum with no margin left
            heapq.heappop(sml_sum)
            heapq.heappush(sml_sum, 6)
        else:
            # max from big_sum with no margin left
            heapq.heappop(big_sum)
            heapq.heappush(big_sum, -1)
    
    return count

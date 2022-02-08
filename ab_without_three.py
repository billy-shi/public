#! /usr/bin/python

"""
A solution programme for an online coding challenge:
Given two integers A and B, return a string which contains 
A number of "a"s and B number of "b"s. But, there cannot be
3 consecutive "a"s or "b"s.

For example, A = 4, B = 1, should give "aabaa", but not "aaaba".

Note the numbers A and B are assumed to have at least one output answer.
Some combinations of A and B give no answer: such as 100 and 1.

Version 1.0

Author: Billy Shi
Date: Feb 8, 2022
"""

def ab_without_three(A, B):
    if A > B and 2*B > A:
        return "aab"*(A-B) + "ab"*(2*B-A)
    elif A > B and 2*B <= A:
        return "a"*(A-2*B) + "baa"*B
    elif B > A and 2*A > B:
        return "bba"*(B-A) + "ba"*(2*A-B)
    elif B > A and 2*A <= B:
        return "b"*(B-2*A) + "abb"*A
    elif A == 0 and B == 0:
        return ""
    elif A == B and A != 0:
        return "ab"*A

# test cases
print(ab_without_three(5, 3))
print(ab_without_three(4, 2))
print(ab_without_three(100, 100))
print(ab_without_three(0, 0))
print(ab_without_three(52, 46))
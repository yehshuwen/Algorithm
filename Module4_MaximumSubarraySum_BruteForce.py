#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@author: Shu-Wen Yeh
from sys import maxsize # import max int for initialization
arr = [15, 13, 8, 14, 12, 9, 10, 15, 9] # initialize the input array
ans = -maxsize - 1 # initialize ans variable to -intmax
# WRITE YOUR CODE HERE

n = len(arr)
if n > 1:
    diff_arr = [arr[i] - arr[i-1] for i in range(1, n)]
    m = len(diff_arr)

    for i in range(m):
        current_sum = 0
        for j in range(i, m):
            current_sum += diff_arr[j]
            if current_sum > ans:
                ans = current_sum
else:
    ans = 0

print(ans) # printing the answer




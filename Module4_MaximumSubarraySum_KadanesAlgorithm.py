#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@author: Shu-Wen Yeh
#@author: Shu-Wen Yeh
arr = [15, 13, 8, 14, 12, 9, 10, 15, 9] # initialize the input array
# WRITE YOUR CODE HERE
n = len(arr)
ans = 0
if n > 1:
    diff_arr = [arr[i] - arr[i-1] for i in range(1, n)]
    m = len(diff_arr)

    max_so_far = diff_arr[0]
    current_max = diff_arr[0]

    for i in range(1, m):
        current_max = max(diff_arr[i], current_max + diff_arr[i])
        max_so_far = max(max_so_far, current_max)
    ans = max_so_far

print(ans) # printing the max possible subarray sum,

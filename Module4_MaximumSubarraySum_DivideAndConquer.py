#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@author: Shu-Wen Yeh
from sys import maxsize # import max int for initialization
arr = [15, 13, 8, 14, 12, 9, 10, 15, 9] # initialize the input array
ans = -maxsize - 1 # initialize ans variable to -intmax
# WRITE YOUR CODE HERE


def max_crossing_sum(arr, low, mid, high):
    current_sum = 0
    left_sum = -maxsize - 1
    for i in range(mid, low - 1, -1):
        current_sum = current_sum + arr[i]
        if current_sum > left_sum:
            left_sum = current_sum

    current_sum = 0
    right_sum = -maxsize - 1
    for i in range(mid + 1, high + 1):
        current_sum = current_sum + arr[i]
        if current_sum > right_sum:
            right_sum = current_sum
            
    return left_sum + right_sum

def max_subarray_sum_recursive(arr, low, high):
    if low == high:
        return arr[low]

    mid = (low + high) // 2

    left_mss = max_subarray_sum_recursive(arr, low, mid)
    right_mss = max_subarray_sum_recursive(arr, mid + 1, high)
    cross_mss = max_crossing_sum(arr, low, mid, high)
    
    return max(left_mss, right_mss, cross_mss)

n = len(arr)
if n > 1:
    diff_arr = [arr[i] - arr[i-1] for i in range(1, n)]
    m = len(diff_arr)
    ans = max_subarray_sum_recursive(diff_arr, 0, m - 1)
else:
    ans = 0


print(ans) # printing the answer

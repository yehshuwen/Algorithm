#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SHU-WEN YEH


''' --- Input values --- '''
M = [ [2, 1, 4, 5, 3],              # Department preference list (indices of programmers)
      [4, 2, 1, 3, 5], 
      [2, 5, 3, 4, 1], 
      [1, 4, 3, 2, 5], 
      [2, 4, 1, 5, 3] ]
W = [ [5, 1, 2, 4, 3],              # Programmer preference list (indices of departments)
      [3, 2, 4, 1, 5], 
      [2, 3, 4, 5, 1], 
      [1, 5, 4, 3, 2], 
      [4, 2, 5, 3, 1] ]
N = 5                               # Number of departments & programmers


# WRITE YOUR CODE HERE
n = N

# Build programmer to department inverse ranking
rankW = [[0]*n for _ in range(n)]
for w in range(n):
    for position, dept_no in enumerate(W[w]):
        rankW[w][dept_no-1] = position

# proposal index
next_idx = [0]*n                    # [0, 0, 0, 0, 0]

# Current programmer match
programmer_match = [-1]*n
# Current department match
dept_match = [-1]*n

from collections import deque

# unmatched department
free_dept = deque(range(n))          # Create 0, 1, 2, 3, 4

while free_dept:
    d = free_dept.popleft()

    if next_idx[d] >= n:
        continue

    w = M[d][next_idx[d]] - 1
    next_idx[d] += 1

    if programmer_match[w] == -1:
        programmer_match[w] = d
        dept_match[d] = w
    else:
        d_curr = programmer_match[w]
        if rankW[w][d] < rankW[w][d_curr]:
            programmer_match[w] = d
            dept_match[d] = w
            dept_match[d_curr] = -1
            free_dept.append(d_curr)
        else:
            if next_idx[d] < n:
                free_dept.append(d)

programmer = [dept_match[d] + 1 for d in range(n)]


''' --- Visualizing the result, Printing the output --- '''
Names = [ ['HR', 'CRM', 'Admin', 'Research', 'Development'],      # Initialize the mapping of names
          ['Adam', 'Bob', 'Clare', 'Diane', 'Emily'] ]
print('Result is:-')
for i in range(N):
    print(Names[0][i], ":", Names[1][programmer[i]-1])                # Map the result to the names

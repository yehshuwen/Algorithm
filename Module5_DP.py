#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Shu-Wen Yeh


w1 = "professor"
w2 = "confession"
ans = 0                                   # initialize ans variable to 0

# WRITE YOUR CODE HERE

# Get lengths of the two strings
n = len(w1)
m = len(w2)

# Initialize the memoization table with -1
memo = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]

# 1-) Recursive DP with memoization
def solve_ed(i, j):
    # Base cases
    if i == 0:
        return j
    if j == 0:
        return i

    # If the subproblem has already been solved, return the stored result
    if memo[i][j] != -1:
        return memo[i][j]

    # If the last characters match, no operation is needed.
    if w1[i - 1] == w2[j - 1]:
        result = solve_ed(i - 1, j - 1)
    else:
        # If the last characters are different, find the minimum cost among the three operations.
        insert_cost = solve_ed(i, j - 1)
        delete_cost = solve_ed(i - 1, j)
        replace_cost = solve_ed(i - 1, j - 1)
        
        # The total cost
        result = 1 + min(insert_cost, delete_cost, replace_cost)
    
    # Store the result in the memoization table
    memo[i][j] = result
    return result

# 2-) Function to backtrack the memoization table and print operations
def print_operations():
    print(f"--- Operations to convert '{w1}' to '{w2}' ---")
    operations = []
    i, j = n, m

    while i > 0 or j > 0:
        if i == 0:
            operations.append(f"Insert '{w2[j-1]}'")
            j -= 1
            continue
        
        if j == 0:
            operations.append(f"Delete '{w1[i-1]}'")
            i -= 1
            continue

        if w1[i - 1] == w2[j - 1]:
            i -= 1
            j -= 1
        else:
            insert_cost = memo[i][j - 1]
            delete_cost = memo[i - 1][j]
            replace_cost = memo[i - 1][j - 1]
            
            min_cost = min(insert_cost, delete_cost, replace_cost)

            if min_cost == replace_cost:
                operations.append(f"Replace '{w1[i-1]}' with '{w2[j-1]}'")
                i -= 1
                j -= 1
            elif min_cost == insert_cost:
                operations.append(f"Insert '{w2[j-1]}'")
                j -= 1
            else:
                operations.append(f"Delete '{w1[i-1]}'")
                i -= 1

    # Print the operations
    for op in reversed(operations):
        print(f"  - {op}")
    print("-" * 50)

ans = solve_ed(n, m)

print_operations()

# -----------------------------------------------------------------------------
print(ans)                                     # printing the answer
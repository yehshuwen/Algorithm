#!/usr/bin/env python3
import random
# -*- coding: utf-8 -*-
#@author: Shu-Wen Yeh
# Date: 2025/12/04

input_text = "algorithms"

# Generate random enumeration of letters (Random Sequential Order)
n = len(input_text)
randomOrder = [None] * n
for i in range(n):
    randomOrder[i] = i    

for i in range(n-1):
    randPos = i + random.randint(0, n-i-1)
    tmp = randomOrder[i];
    randomOrder[i] = randomOrder[randPos];
    randomOrder[randPos] = tmp;


for i in range(n):
    pick = randomOrder[i]
    print (pick)

    # WRITE YOUR CODE HERE
    if i == 0:
        text_list = list(input_text)
        moved = [False] * n

    if not moved[pick]:
        swap_idx = pick + random.choice([-1, 1])

        if 0 <= swap_idx < n:
            if not moved[swap_idx]:
                text_list[pick], text_list[swap_idx] = text_list[swap_idx], text_list[pick]
                
                moved[pick] = True
                moved[swap_idx] = True


print("Result: " + "".join(text_list))
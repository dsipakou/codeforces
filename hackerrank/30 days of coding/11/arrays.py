#!/bin/python3

import sys


arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)
output = -64
for i in range(4):
    for j in range(4):
        output = max(output, sum(arr[j][i:i + 3]) + arr[j + 1][i + 1] + sum(arr[j + 2][i:i + 3]))
print(output)

import math
import os
import random
import re
import sys

def solve(n , k, score):
    count = 0
    for i in range(n):
        if score[i] > 0 and score[i]>=score[k-1]:
            count+=1
        else:
            count+=0
    return count
    
if __name__ == '__main__':
    n, k = list(map(int, input().strip().split()))
    score = list(map(int, input().strip().split()))
    print(solve(n, k ,score))
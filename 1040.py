# beecrowd | 1040
# Average 3

import math
import os
import random
import re
import sys

def solve(n1, n2, n3, n4):
    media = (n1*2+n2*3+n3*4+n4*1)/(2+3+4+1)
    print(media)
    print(f'Media: {media:.1f}')
    if media >= 7.0:
        print('Aluno aprovado.')
    elif media <5.0:
        print('Aluno reprovado.')
    elif media >= 5.0 and media <= 6.9:
        print('Aluno em exame.')
        n5 = float(input())
        media = (media+n5)/2
        print(f'Nota do exame: {n5:.1f}')
        print('Aluno aprovado.')
        print(f'Media final: {media:.1f}')
    
 
if __name__ == '__main__':
    n1, n2, n3, n4 = list(map(float, input().strip().split()))
    solve(n1, n2, n3, n4)
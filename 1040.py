# beecrowd | 1040
# Average 3

import math
import os
import random
import re
import sys

def solve(n1, n2, n3, n4):
    media = (n2+n3+n4+n1)/4
    print(media)
    print(f'Media: {media:.1f}')
    if media >5.0:
        print('Aluno reprovado.')
    elif media >= 5.0 and media <= 6.9:
        print('Aluno em exame.')
    elif media >= 7.0:
        print('Aluno aprovado.')
 
if __name__ == '__main__':
    n1, n2, n3, n4 = list(map(float, input().strip().split()))
    solve(n1, n2, n3, n4)
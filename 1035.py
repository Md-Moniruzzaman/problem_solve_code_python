a, b, c, d = list(map(int, input().split()))

if a%2 == 0 and c>=0 and d >=0 and b>c and d>a and (c + d) > (a + b):
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
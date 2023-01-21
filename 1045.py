# beecrowd | 1045
# Triangle Types

li = list(map(float, input().strip().split()))
li.sort(reverse=True)

a = li[0]
b = li[1]
c = li[2]

if a>= (b+c):
    print('NAO FORMA TRIANGULO')
elif a**2 == (b**2 + c**2):
    print('TRIANGULO RETANGULO')
elif a**2 > (b**2 + c**2):
    print('TRIANGULO OBTUSANGULO')
elif a**2 < (b**2 + c**2):
    print('TRIANGULO ACUTANGULO')

if a == b == c :
    print('TRIANGULO EQUILATERO')
elif a == b !=c or a!=b==c or a == c !=b:
    print('TRIANGULO ISOSCELES')

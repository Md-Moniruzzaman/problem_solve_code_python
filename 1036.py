# beecrowd | 1036
# Bhaskara's Formula
a, b, c = list(map(float, input().split()))

formula = b**2 - 4*a*c

if a == 0 or formula<0:
   print('Impossivel calcular')
else:
    X1 = (-b + formula**0.50)/(2*a)
    X2 = (-b - formula**0.50)/(2*a)
    print(f'R1 = {X1:.5f}')
    print(f'R2 = {X2:.5f}')
    
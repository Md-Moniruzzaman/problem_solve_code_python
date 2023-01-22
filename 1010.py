# beecrowd | 1010
# Simple Calculate

a = [int(n) if n.isdigit() else float(n) for n in input().strip().split()[1:]]
b = [int(n) if n.isdigit() else float(n) for n in input().strip().split()[1:]]

pay = a[0]*a[1] + b[0]*b[1]
print(f'VALOR A PAGAR: R$ {pay:.2f}')
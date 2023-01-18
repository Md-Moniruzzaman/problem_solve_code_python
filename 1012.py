a, b, c = list(map(float, input().split()))
area = 3.14159*c**2
tri = .5*a*c
trap = 0.5*(a+b)*c
sqr = b**2
rect = a*b

print(f'''TRIANGULO: {tri:.3f}
CIRCULO: {area:.3f}
TRAPEZIO: {trap:.3f}
QUADRADO: {sqr:.3f}
RETANGULO: {rect:.3f}''')

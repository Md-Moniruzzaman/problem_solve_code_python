
tk = float(input())

print('NOTAS:')
for x in [100, 50, 20, 10, 5, 2]:
    print(f'{int(tk/x)} nota(s) de R$ {x}.00')
    tk = float(f'{tk%x:.2f}')

print('MOEDAS:')
for x in [1, 0.50, 0.25, 0.10, 0.05, 0.01]:
    print(f'{int(tk/x)} moeda(s) de R$ {x:.2f}')
    tk = float(f'{tk%x:.2f}')
    
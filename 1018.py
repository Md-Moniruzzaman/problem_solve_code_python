tk = int(input())
note = [100, 50, 20, 10, 5, 2 , 1]
print(tk)

for x in note:
    print(f'{tk//x} nota(s) de R$ {x},00')
    tk = tk % x
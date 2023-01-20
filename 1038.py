x, y = list(map(int, input().split()))

prod_dic = {1: 4.00, 2: 4.50, 3: 5.00, 4 : 2.00, 5: 1.50}

pay = prod_dic[x]*y

print(f'Total: R$ {pay:.2f}')
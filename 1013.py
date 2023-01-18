a, b, c = list(map(int, input().split()))
if a>b:
    if a>c:
        print(f'{a} eh o maior')
    elif c>b:
        print(f'{c} eh o maior')
elif b>c:
    print(f'{b} eh o maior')
else:
     print(f'{c} eh o maior')
# b = max(a)

# print(f'{b} eh o maior')
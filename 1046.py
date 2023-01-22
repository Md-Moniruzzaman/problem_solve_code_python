st, en = list(map(int, input().strip().split()))

if st>en:
    duration = (24 - st) + en
    print(f'O JOGO DUROU {duration} HORA(S)')
elif st == en:
    print(f'O JOGO DUROU 24 HORA(S)')
else:
    duration = en - st
    print(f'O JOGO DUROU {duration} HORA(S)')
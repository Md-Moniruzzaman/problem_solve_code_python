# beecrowd | 1047
# Game Time with Minutes

st,sm,et,em = list(map(int, input().strip().split()))

duration = ((et*60)+em)-((st*60)+sm)

if duration<= 0:
    duration+=24*60

hour = duration//60
minit = duration%60
print(f'O JOGO DUROU {hour} HORA(S) E {minit} MINUTO(S)')
    

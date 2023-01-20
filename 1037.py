# beecrowd | 1037
# Interval

i = float(input())

if i>=0 and i<=100:
    if i>=0 and i<=25.00:
        print('Intervalo [0,25]')
    elif i>25.00 and i<=50.00:
        print('Intervalo (25,50]')
    elif i>50.00 and i<=75.00:
        print('Intervalo (50,75]')
    elif i>75.00 and i<=100.00:
        print('Intervalo (75,100]')
else:
    print('Fora de intervalo')
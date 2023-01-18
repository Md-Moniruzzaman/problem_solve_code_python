# beecrowd | 1015
# Distance Between Two Points

def distance(x1,x2,y1,y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    

x1, y1 = list(map(float, input().split()))
x2, y2 = list(map(float, input().split()))

# dis = ((x1 - x2)**2 + (y1 - y2)**2)**0.5

print(f'{distance(x1,x2,y1,y2):.4f}')
# beecrowd | 1017
# Fuel Spent

def calculate_liter(h,asp):
    return (h*asp)/12

h = int(input())
asp = int(input())

print(f'{calculate_liter(h,asp):.3f}')


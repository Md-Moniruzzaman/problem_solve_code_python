tic = int(input('Please enter your value:'))
def row(s, n):
    return s * n
i=0

while i<tic:
    
    print(row('___ ', tic))
    print(row('|  ', tic+1))
    i+=1 
print(row('--- ', tic))
from audioop import reverse
list = [1,6,4,4,5,16,12,4]
b = False
c = False
count = 0
counter1 = 0
list.sort(reverse=True)
print(list)
list1 = list
list1.sort()
print(list1)
b = False
for x in range(len(list1)):
    if list1[x]+list[x] != 20:
        b = True
        

print(b)

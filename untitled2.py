a = [2,4,5,5,4,4,3]

total = 0

for i in a:
    total+=i

stn = 0
for j in range(len(a)):
    right = total - stn - a[j]
    
    if right == stn:
        print(j)
    stn+=a[j]
arr = [-2, -3, -4, -1, -2, -1, -5, -3]

max_till_now = 0
max_sum = 0

for i in range(len(arr)):
    max_sum = max_sum + arr[i]
    if max_sum<0:
        max_sum = 0
    if max_sum > max_till_now:
        max_till_now = max_sum
        

print(max_till_now)
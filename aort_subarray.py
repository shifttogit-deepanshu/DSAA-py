arr = [1,2,3,4,5,8,7,6,9,10,11]



def subarr(arr):
    if len(arr)<1:
        return (-1,-1)
    s_i = -1
    e_i = -1
    smallest= 100000000000000
    largest = -10000000000000
    for i in range(1,len(arr)-1):
        if arr[i]>arr[i+1]:
            largest = max(arr[i],largest)
        if arr[i]<arr[i-1]:
            smallest = min(arr[i],smallest)
                
    for i in range(1,len(arr)-1):
        if largest > arr[i-1] and largest<=arr[i]:
            s_i = i
        if smallest > arr[i-1] and largest<=arr[i]:
            e_i = i
    if arr[0]>smallest:
        s_i = 0
    if arr[len(arr)-1]<largest:
        e_i = len(arr)-1
    
    for i in range(1,len(arr)-1):
        if arr[i]>smallest and arr[i-1]<smallest:
            s_i = i
        if arr[i]>largest and arr[i-1]<largest:
            e_i = i
            
    
    print(s_i,e_i)
subarr(arr)
arr1 = [23,5,10,17,30]
arr2 = [26,134,135,14,19]

def min_diff(arr1,arr2):
    arr1.sort()
    arr2.sort()
    
    diff = 10000000000000
    i = j = 0
    while i<len(arr1) and j<len(arr2):
        if abs(arr1[i]-arr2[j])<diff:
            diff = abs(arr1[i]-arr2[j])
        
        if arr1[i]<arr2[j]:
            i+=1
        else:
            j+=1
    
    print(diff)
    
min_diff(arr1,arr2)
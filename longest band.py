arr = [1,9,3,0,18,5,2,4,7,8,11,12,6,10,0,56,34,7,5,7,4,7,45,12,6,788,45,87]


    
def longest_band(arr):      
    longest = 0
    longest_arr = []
    for i in range(0,len(arr)):
        if not arr[i]-1 in arr:
            head = arr[i]
            curr_len = 1
            curr_arr = [head]
            while head+1 in arr:
                curr_arr.append(head+1)
                curr_len+=1
                head+=1
        
            if curr_len>longest:
                longest = curr_len
                longest_arr = curr_arr
    
    print(longest_arr)
    

longest_band(arr)


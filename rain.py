arr = [0,1,0,2,1,0,1,3,2,1,2,1]

def rain(arr):
    sum = 0  
    for i in range(1,len(arr)-1):
        if arr[i]<arr[i+1] and arr[i]<arr[i-1]:
            start_arr = [arr[i]]
            end_arr = []
            j = i
            while arr[j]<arr[j-1] and j>=0:
                j-=1
                start_arr.append(arr[j])                
            while arr[i]<arr[i+1] and i<=len(arr)-2:
                i+=1
                end_arr.append(arr[i])                
            low = min(max(start_arr),max(end_arr))
            
            for s in start_arr:
                if s<low:
                    sum+=low-s
            for e in end_arr:
                if e<low:
                    sum+=low-e
    print(sum)
            
            
rain(arr)


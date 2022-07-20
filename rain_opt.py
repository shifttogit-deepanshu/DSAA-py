arr = [0,1,0,2,1,0,1,3,2,1,2,1]

def rain(arr):
    start_arr = []
    end_arr = []
    start = 0
    end = 0
    s=0
    for i in range(len(arr)): 
        
        start_elem = arr[i]
        if start_elem>start:
            start = start_elem
        start_arr.append(start)
        
        
        end_pos = len(arr)-1-i
        end_element = arr[end_pos]
        if end_element>end:
            end = end_element
        end_arr.insert(0,end)
            
    for i in range(len(arr)):
        s+=min(start_arr[i],end_arr[i]) - arr[i] 
        
    print(s)
    
rain(arr)

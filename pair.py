arr = [10,5,2,3,-6,11]

S = 4

def pair(arr,s):
    result = []
    diff_dict = []   
    for i in range(len(arr)):             
        diff = s - arr[i]
        if diff in diff_dict:
            result.append((arr[i],diff))
        diff_dict.append(arr[i])
            
            
    print(result)
        

pair(arr,S)
    
    
arr = [2,3,4,5,6,7,8,9,15]

s = 20

def triplets(arr,s): 
    arr.sort()
    result = []
    for i in range(len(arr)-3):        
        f = arr[i]
        pair = s-f
        start = i+1
        end = len(arr)-1
        flag=0
        while start<end and flag==0:
            print(arr[i],arr[start],arr[end])
            if arr[start] + arr[end] == pair:
                result.append((arr[i],arr[start],arr[end]))      
                flag=1
            elif arr[start] + arr[end] > pair:               
                end-=1
            elif arr[start] + arr[end] < pair:
                start+=1           
        
    print(result)
    
    
triplets(arr,s)
    



str1 = "coding is fun"
str2 = "cotsun"

def compute(str1,str2):
    i=j=0
    while i<len(str1) and j<len(str2):
        if str1[i]==str2[j]:
            j+=1
            i+=1
        else:
            i+=1
        
    if j==len(str2):
        return True
    else:
        return False
    
    
    
print(compute(str1,str2))
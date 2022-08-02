stri = "bbbaaxdddddddeeeff"

def enc(stri):
    dict = {}
    
    for i in range(len(stri)):
    
        if stri[i] in dict:
            dict[stri[i]]+=1
        else:
            dict[stri[i]] = 1
    
    
    output = ""
    for i in dict:
        output+=i+str(dict[i])
        
    if len(output)<len(stri):
        return output
    
    return stri

print(enc(stri))
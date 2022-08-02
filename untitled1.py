str = "abc"

def rec(string,ini,arr):   

    
    if len(string)<1:
        arr.append(ini)
        return 
    
    ch = string[0]
    newstring = string[1:]    
    
    rec(newstring,ini+ch,arr)
    
    rec(newstring,ini,arr)
    

vec = []    
rec("abc","",vec)

print(vec)
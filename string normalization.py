inp = "This is so     Much fun!"

new_str = ""

i = 0

while i<(len(inp)):
    if inp[i]==" " and inp[i+1].islower():
        new_str+=" " + inp[i+1].upper()
        i+=2
    elif inp[i]==" " and inp[i+1]==" ":
        i+=1
        continue;
    else:
        new_str+=inp[i]
        i+=1
        
print(new_str)
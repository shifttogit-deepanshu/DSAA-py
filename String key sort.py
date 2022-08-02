string = "92 022\n82 12\n77 13"

def getTok(stri, index):
    key = 0
    s = ""
    while index>1 :
        if stri[key]==" ":
            index-=1
        key+=1
    while (key<len(stri)) and (not stri[key]==" ") :   
        s+=stri[key]  
        key+=1
    return s
            
    
def calc(strin,num1,boolean,ordering):
    forsort = []
    res_arr = []
    dict = {}
    outarr = strin.split("\n")
    for i in range(len(outarr)):
        if ordering=="numeric":
            res = int(getTok(outarr[i], num1))
        elif ordering=="lexo":
            res = getTok(outarr[i], num1)
        forsort.append(res)
        dict[res] = outarr[i]
    forsort.sort(reverse=boolean)
    for i in forsort:
        res_arr.append(dict[i])
    print("\n".join(res_arr))
    
calc(string,2,False,"numeric")
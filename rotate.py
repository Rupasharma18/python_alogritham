def rotate(input,d): 
    Lfirst = input[0 : d] 
    Lsecond = input[d :] 
    return Lsecond + Lfirst
input =[1, 2, 3, 4, 5]
d=4
print (rotate(input,d)) 
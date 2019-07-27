def decimal(num):
    b = ""
    while num > 0:
        b = b+str(num %2) 
        num = num // 2
    return (b)    
user = int(input("enter your num")) 
print (decimal(user))
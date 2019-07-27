# list1 =[10, 20, 20, 10, 10, 30, 50, 10, 20]
from collections import Counter
def sockMerchant(n, ar):
    sum=0
    for values in Counter(ar).values():
        # print (Counter(ar))
        sum+=values//2
    return sum
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]    
n = 7
print (sockMerchant(n, ar))
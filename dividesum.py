def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(n-1):
        j = i+1
        while j < n:
            if ((ar[i] + ar[j]) % k) == 0:
                count += 1
            j += 1
    return count
print (divisibleSumPairs(2,2,[8,10]))    
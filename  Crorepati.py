rupess = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
i = 0 
print (len(rupess))
corepati = 0
lakepati = 0
dilwale = 0
while i < len(rupess):
    if rupess[i] > 100000000 or rupess[i] == 100000000:
        corepati = corepati+ 1
    elif rupess[i] > 1000000 or rupess[i] == 1000000:
        lakepati = lakepati + 1
    else:
        dilwale = dilwale + 1
    i = i + 1

print  (corepati)
print (lakepati)
print(dilwale)        
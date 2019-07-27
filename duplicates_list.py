n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
i = 0
new_list = []
while i < len(n):
    if n[i] not in  new_list:
        new_list.append(n[i])
    i = i + 1
print (new_list)         
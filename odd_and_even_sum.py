elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i = 0
odd_sum = 0
even_sum = 0
while i < len(elements):
    if elements[i] % 2 == 0:
        even_sum = even_sum + elements[i]
    elif elements[i] % 2 != 0 :
        odd_sum = odd_sum + elements[i]
    i = i + 1
print ('even_sum_number:-', even_sum)
print ('odd_sum_number:-', odd_sum)            
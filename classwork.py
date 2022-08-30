arr = [2, 2, 3, 4]
arr_a = [1, 2, 2, 3, 3, 3]
frequency = {}

for x in arr_a:
    if x in frequency:
        frequency[x] += 1 
    else:
        frequency[x] = 1
print(frequency)

for val in frequency:
    if val == 2:
        print(frequency[val])

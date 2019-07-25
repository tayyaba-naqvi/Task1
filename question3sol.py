arr = []

for i in range(1501, 2700):
    if i % 5 == 0 and i % 7 == 0:
        arr.append(i)

print(arr)

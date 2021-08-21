from collections import defaultdict

arr = dict()

if 1 in arr:
    arr[1].append(3)
else:
    arr[1] = [3]

print(arr)
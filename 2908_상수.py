a,b = input().split()
arr1 = []
arr2 = []
length1 = len(a)
length2 = len(b)
for x in range(length1):
    arr1.append(a[x])
arr1.reverse()
for x in range(length2):
    arr2.append(b[x])
arr2.reverse()
x = int(''.join(arr1))
y = int(''.join(arr2))
if x > y:
    print(x)
else:
    print(y)

def binary(arr,target):
    if len(arr) < 2:
        return
    mid = len(arr)//2
    print(arr, arr[mid], target)
    if arr[mid] == target:
        print('target done')
    else:
        print('target none')
    if target < arr[mid]:
        binary(arr[:mid],target)
    if target > arr[mid]:
        binary(arr[mid:],target)


arr = []
target = 20
for x in range(50):
    arr.append(x)

binary(arr, target)
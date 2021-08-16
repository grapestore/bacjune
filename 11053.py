import sys



num = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
result = []
for i in range(num):
    count = 1
    visited = []
    visited.append(arr[i])
    if arr[i] not in arr[:i]:
        for j in range(i+1,num):
            if arr[j] not in visited:
                if arr[j] > visited[-1]:
                    visited.append(arr[j])
                else:
                    visited.pop()
                    visited.append(arr[j])
    result.append(len(visited))
print(max(result))

##### 못품 나중에 재도전######

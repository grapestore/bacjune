import sys
sys.stdin = open('inputs.text')

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
m = max(arr)

for i in range(n):
    arr[i] = arr[i]/m*100

print(sum(arr)/n)
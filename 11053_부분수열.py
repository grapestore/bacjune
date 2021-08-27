import sys
sys.stdin = open('inputs.text')

n = int(sys.stdin.readline().rstrip())
memo = [1] * (n)
arr = list(map(int,sys.stdin.readline().split()))

for i in range(1,n):
    for j in range(i):
        if arr[j]<arr[i]:
            memo[i] = max(memo[i], memo[j]+1)
print(max(memo))
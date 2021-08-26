import sys
sys.stdin = open('inputs.text')

n = int(sys.stdin.readline())

memo = {0:0, 1:1, 2:2}

def fx(n):
    if n in memo:
        return memo[n]

    memo[n] = (fx(n-2) + fx(n-1))%15746
    return memo[n]


for i in range(3,n+1):
    #memo[i] = (memo[i-2] + memo[i-1])%15746
    fx(i)


print(fx(n))
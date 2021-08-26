import sys
sys.stdin = open('inputs.text')

n = int(sys.stdin.readline())

memo = {1:1, 2:1}

def fx(n):
    if n in memo:
        return memo[n]
    memo[n] = fx(n-1) + fx(n-2)
    return memo[n]


print(fx(n))
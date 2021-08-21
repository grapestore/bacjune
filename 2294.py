from collections import deque
import sys
#sys.stdin = open('inputs.text')

n, k = map(int, sys.stdin.readline().split())
# coins = []
# for _ in range(n):
#     coins.append(int(input()))
# set(coins)
coins = set(list(int(sys.stdin.readline()) for _ in range(n)))
check = [0 for _ in range(k+1)]
queue = deque()
for coin in coins:
    if coin > k:
        continue
    queue.append([coin,1])
    check[coin] = 1
    
stable = True
while queue:
    val, cnt = queue.popleft()
    if val == k:
        print(cnt)
        stable = False
        break
    for coin in coins:
        if val + coin > k:
            continue
        if check[val+coin] == 0:
            check[val+coin] = 1
            queue.append([val+coin, cnt+1])


if stable:
    print(-1)
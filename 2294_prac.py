from collections import deque
import sys
#sys.stdin = open('inputs.text')

n, target = map(int, sys.stdin.readline().split())
check_list = [0 for _ in range(target+1)]
# coins = []
# for _ in range(n):
#     coins = coins + list(map(int,sys.stdin.readline().split()))
coins = set(list(int(sys.stdin.readline()) for _ in range(n)))

stable = True
queue = deque()

for coin in coins:
    if coin == target:
        stable == False
        print(1)
        break
    elif coin < target:
        queue.append([coin,1])
        check_list[coin] = 1

while queue:
    value, cnt = queue.popleft()
    if value == target:
        stable = False
        print(cnt)
        break
    for coin in coins:
        if coin+value <= target and check_list[coin+value] == 0:
            check_list[coin+value] = 1
            queue.append([value+coin,cnt+1])

if stable:
    print(-1)
import sys
sys.stdin = open('inputs.text')

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
city_price = list(map(int,sys.stdin.readline().split()))
curr_price = 10000000000
cost = 0
for x in range(len(city_price)-1):
  if curr_price > city_price[x]:
    curr_price = city_price[x]
  cost += curr_price * arr[x]
print(cost)
import sys
sys.stdin = open('inputs.text')


n = int(sys.stdin.readline())

def eratosthenes(N):
  global nums
  nums = [1] * (N+1)

  nums[0] = 0
  nums[1] = 0

  for i in range(N+1):
    nums[i] = i

  for i in range(2, int(N**0.5)+1):
    if nums[i]:
      for j in range(i*i, N+1, i):
        # 앞에 소수가 바꾼건 바꾸지 않겠다 # 
        if nums[j] == j:
          nums[j] = i
  
def find(N):
  result = []

  while(N>1):
    result.append(nums[N])
    N = N//nums[N]

  return result
    


eratosthenes(n)
for data in find(n):
  print(data)

# import math

# num = int(input())

# # 분해가 전부 될때까지 loop 돌립니다.
# while num != 1:
#     for i in range(2, num + 1):
#         # 나눠지면 출력하고,
#         # 다음을 위해 해당 수로 num을 나눠줍니다.
#         if(num % i == 0):
#             print(i)
#             num = num // i
#             break
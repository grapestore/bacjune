# 3의 거듭 제곱수는 3을 b번 곱한 수를 의미하며 3b 형태로 표현합니다. 30 = 1이 성립하며, 31 = 3, 32 = 9, 33 = 27, 34 = 81... 모두 거듭 제곱수입니다.
# 3의 거듭 제곱수를 임의로 더하여 거듭 제곱수 사이에 들어가는 수를 만들 수 있습니다. 예를 들어,

# 4 = 1 + 3
# 31 = 27 + 3 + 1
# 입니다.
# 이때, 같은 거듭 제곱수를 2번 이상 더할 수는 없습니다. 이러한 규칙으로 만들어낼 수 있는 수와 3의 거듭 제곱수를 합쳐서 순서대로 배치하면 1, 3, 4, 9, 10...이 됩니다. 이렇게 배치한 숫자의 n번째 숫자가 무엇인지를 알려주는 함수 solution 을 완성해주세요.

# 제한사항
# n은 1 ≤ n ≤ 1010 인 자연수



# def solution(n):
#     answer = 0
#     dp = [1]
#     before = 1
#     length = 1
#     while True:
#         temp = before * 3
#         dp.append(temp)
#         length += 1
#         temp_len = length - 1
#         for j in range(temp_len):
#             dp.append(temp+dp[j])
#             length+=1
#             if length > n:
#                 return dp[n-1]
#         before = temp

def dfs(x,y,cnt, target):

    if cnt == 2*target:
        result.append(1)
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<target and 0<=ny<2 and visit[ny][nx] == False:
            visit[ny][nx] = True
            dfs(nx,ny,cnt+1,target)
            visit[ny][nx] = False


N = 10

result = []
answer = 0
visit = [[False] * N for _ in range(2)]
visit[0][0] = True
dfs(0,0,1, N)
print(result)
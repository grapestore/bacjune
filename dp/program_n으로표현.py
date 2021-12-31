def dfs(count, num,target):
    global result
    if count > 8:
        return
    if num == target:
        if count < result:
            result = count
    for i in range(8):
        dfs(count+i+1, num+NNN[i], target)
        dfs(count+i+1, num-NNN[i], target)
        dfs(count+i+1, num*NNN[i], target)
        dfs(count+i+1, num/NNN[i], target)
        
    return

def solution(N, number):
    global NNN, result
    strN = str(N)
    NNN = []
    result = 9
    temp = strN
    for _ in range(8):
        NNN.append(int(temp))
        temp+=strN

    dfs(0, 0, number)
    print(result)
    if result>8:
        return -1
    else:
        return result




# from collections import deque

# def bfs(target):
#     global result
#     queue = deque([[0,0]])
    
#     while queue:
#         count, num = queue.popleft()
#         if count>8:
#             continue
#         if count>result:
#             break
#         if num == target:
            
#             result = count
        
#         for i in range(8):
#             queue.append([count+i+1, num+NNN[i]])
#             queue.append([count+i+1, num-NNN[i]])
#             queue.append([count+i+1, num*NNN[i]])
#             queue.append([count+i+1, num//NNN[i]])
        
#     return

# def solution(N, number):
#     global NNN, result
#     strN = str(N)
#     NNN = []
#     result = 9
#     temp = strN
#     for _ in range(8):
#         NNN.append(int(temp))
#         temp+=strN

#     bfs(number)
#     print(result)
#     if result>8:
#         return -1
#     else:
#         return result

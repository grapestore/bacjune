import string
from collections import deque

def solution(name):
    global alpha
    answer = []
    alpha_arr = []
    alpha = {}
    for i,x in enumerate(string.ascii_uppercase):
        alpha_arr.append(x)
        alpha[x] = i
    result=[]
    queue = deque(map(str,name))
    cur = 'A'
    index = 0
    while queue:
        find = queue.popleft()
        c1,c2 = index,index
        temp = []
        cnt = 0
        while alpha_arr[c1] != find:
            c1 += 1
            c1 %= 26
            cnt += 1
        temp.append(cnt)
        cnt=0
        while alpha_arr[c2] != find:
            c2 -= 1
            cnt += 1
        temp.append(cnt)
        
        c3,c4 = 0,-1
        cnt = 1
        while alpha_arr[c3] != find:
            c3 += 1
            c3 %= 26
            cnt+=1
        temp.append(cnt)
        cnt = 1
        while alpha_arr[c4] != find:
            c4 -= 1
            cnt+=1
        temp.append(cnt)

        result.append(min(temp))
        index = alpha[find]
    print(sum(result))
    return sum(result)

if __name__ == "__main__":
	solution("JAN")
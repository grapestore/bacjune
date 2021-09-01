import sys
sys.stdin = open('inputs.text')
from collections import deque


a,n = map(int,sys.stdin.readline().split())
multi = deque(map(int,sys.stdin.readline().split()))
result = []
while len(result) < a:
    real_temp = multi.popleft()
    if real_temp not in result:
        result.append(real_temp)
count = 0
while multi:
    temp = multi.popleft()
    if temp not in result:
        tete = []
        for i in range(len(multi)):
            if multi[i] in result and multi[i] not in tete:
                tete.append(multi[i])
        if len(tete) == 0:
            result[0] = temp
            count+=1
        else:
            nocount = 0
            for x in range(len(result)):
                if result[x] not in tete:
                    result[x] = temp
                    nocount+=1
                    count+=1
                    break
            if nocount == 0:
                inser = tete[-1]
                result[result.index(inser)] = temp
                count+=1

print(count)
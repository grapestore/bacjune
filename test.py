import sys
from collections import deque
sys.stdin = open('inputs.text')

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())

partList = [0] * (N + 1)

midPart = []
needPart = [[] for _ in range(N + 1)]

for _ in range(M):
    X, Y, K = map(int, sys.stdin.readline().strip().split())
    if X not in midPart and X != N:
        midPart.append(X)
    needPart[X].append([Y, K])

midQue = deque(midPart)

def doWork():
    
    while midQue:
        midPop = midQue.popleft()
        if needPart[midPop] == []:
            continue

        for p in needPart[midPop]:
                partList[p[0]] += (p[1] * partList[midPop])
                if p[0] in midPart:
                    midQue.append(p[0])
        partList[midPop] = 0


for p in needPart[N]:
    partList[p[0]] += p[1]
    partList[N] = 0

doWork()

for i in range(1, len(partList)):
    if partList[i] == 0:
        continue

    print(i, partList[i], sep= ' ')
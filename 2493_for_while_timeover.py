import sys

num = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
stk = []
for i in range(num):
    stk.append([i+1,arr[i]])
result = []
answer = ''
for x in stk:
    if len(result) < 1:
        answer += str(0) + ' '
        result.append(x)
    else:
        try:
            while result[len(result)-1][1] < x[1] and len(result) > 0:
                result.pop()
            answer += str(result[len(result)-1][0]) + ' '
            result.append(x)
        except:
            if len(result) < 1:
                answer += str(0) + ' '
            if len(result) < 1 or result[len(result)-1][1] > x[1]:
                result.append(x)
# j = ''
# for k in answer:
#     j = str(j) + ' ' + str(k)
# print(j[1:])
print(answer)
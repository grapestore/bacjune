from collections import defaultdict

def solution(s):
    answer = []
    info = defaultdict(int)
    temp = ''
    for x in s:
        if x.isnumeric():
            temp += x
        elif (x == ',' or x == '}') and temp.isnumeric():
            info[temp] += 1
            temp = ''
    result = []
    for x in info:
        result.append([info[x],x])
    result = sorted(result, key=lambda x : -x[0])
    for y in result:
        answer.append(int(y[1]))
    return answer
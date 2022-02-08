from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    info = defaultdict(int)
    for x in orders:
        for i in range(2,len(x)+1):
            for permu in combinations(sorted(x),i):
                temp = ''.join(permu)
                info[temp] += 1
    answer = []
    
    for idx in course:
        result = []
        for find in info:
            if len(find) == idx and info[find]>1:
                if len(result) == 0:
                    result.append(find)
                    continue
                if info[result[-1]] < info[find]:
                    result = [find]
                elif info[result[-1]] == info[find]:
                    result.append(find)
        for k in result:
            answer.append(k)


    return sorted(answer)
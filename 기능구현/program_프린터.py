from collections import deque

def solution(priorities, location):
    answer = 0
    prio = deque(priorities)
    compare = deque()
    for i in range(len(priorities)):
        compare.append(i)
    find = compare[location]
    cnt = 0
    while prio:
        cur_p = prio.popleft()
        cur = compare.popleft()
        status = True
        for check in prio:
            if check>cur_p:
                status = False
                break
        if status:
            cnt += 1
        else:
            prio.append(cur_p)
            compare.append(cur)
        if status and cur == find:
            return cnt
            

    return answer
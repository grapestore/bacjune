import sys

def dfs(graph, start_node):
    visit = []
    stack = []
    global count, maximum
    
    stack.append(start_node)
    while stack:
        node = stack.pop()
        if node not in visit:
            if visit_check[node] == False:
                visit_check[node] = True
                visit.append(node)
                stack.extend(graph[node])
    count += 1
    if count > maximum:
        maximum = count

    return count

if __name__ == '__main__':
    arr = []
    arr = [[9, 9, 9, 9, 9, 9, 9]
            [9, 2, 1, 2, 1, 2, 9]
            [9, 1, 8, 7, 8, 1, 9]
            [9, 2, 7, 9, 7, 2, 9]
            [9, 1, 8, 7, 8, 1, 9]
            [9, 2, 1, 2, 1, 2, 9]
            [9, 9, 9, 9, 9, 9, 9]]
    a_app = arr.append
    num = int(sys.stdin.readline())
    # for ins in range(num):
    #     for zzz in map(int,sys.stdin.readline().split()):
    #         a_app(zzz)
    check = dict()
    level = 0
    count = 0
    maximum = 0
    discount = min(arr)-1
    for qwer in range(num**2):
        arr[qwer] -= discount
    for x in range(len(arr)):
        tmp = []
        append = tmp.append
        if x-1 >= 0:
            if x>0 and x%num != 0: 
                append(x-1) 
        if(x+1)%num != 0:
            append(x+1)
        if x-num > 0:
            append(x-num)
        if x+num < len(arr):
            append(x+num)
        check[x] = tmp
        
        
    #print(check)
    # for del_left in range(0,len(arr),num):
    #     check[del_left].pop(0)
    # for del_right in range(num-1,len(arr),num):
    #     check[del_right].pop(1)
    
    while level < max(arr):
        visit_check = [True] * num**2
        for height_check in range(len(arr)):
            if level < arr[height_check]:
                visit_check[height_check] = False

        count = 0
        
        for next in range(num**2):
            if visit_check[next] == False:
                if arr[next] > level:
                    dfs(check, next)
        level += 1
    print(maximum)
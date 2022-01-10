
def solution(N, trees):
    
    answer = 1
    tree = sorted(trees, key = lambda x : -x[1]) 
    basex,basey = tree.pop()
    while tree:
        x,y = tree.pop()
        if x<basex:
            answer += 1
            basex = x

    return answer
import math

def game(k,a,b,depth):
    
    if depth == k:
        return depth
    
    if a%2 == 0 and a-b == 1:
        return depth
    elif a%2 == 1 and b-a == 1:
        return depth
    else:
        return game(k,math.ceil(a/2),math.ceil(b/2),depth+1)
        

def solution(n,a,b):
    k=1
    while True:
        if n == 2**k:
            break
        k += 1

    return game(k,a,b,1)

if __name__ == "__main__":
  print(solution(8,4,7))
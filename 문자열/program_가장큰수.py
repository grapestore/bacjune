from itertools import permutations

def solution(numbers):
    answer = ''
    maxi = 0
    arr = [x for x in map(str,numbers)]
    arr.sort(key = lambda x: x*3, reverse=True)
    answer = str(int(''.join(arr)))
    
    return answer
from itertools import permutations

## string 숫자인경우 숫자의 순서대로 정렬된다는것을 이용

def solution(numbers):
    answer = ''
    maxi = 0
    arr = [x for x in map(str,numbers)]
    arr.sort(key = lambda x: x*3, reverse=True)
    answer = str(int(''.join(arr)))
    
    return answer
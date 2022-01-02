def dfs(nums, depth, target, length):
    global arr, answer
    if depth == length:
      if nums == target:
        return 1
      else:
        return 0
    cur = arr[depth]
    return dfs(nums+cur,depth+1,target,length) + dfs(nums-cur,depth+1,target,length)

def solution(numbers, target):
    global arr
    arr = numbers
    answer = dfs(0,0,target,len(numbers))
    return answer
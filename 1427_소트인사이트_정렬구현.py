import sys
sys.stdin = open('inputs.text')

que = list(sys.stdin.readline().rstrip())
q = list(map(int,que))


def merge_sort(arr):
  if len(arr) == 1:
    return arr
  end = len(arr)
  mid = end//2
  result = []
  left_loca = 0
  right_loca = 0
  left = merge_sort(arr[:mid])
  right = merge_sort(arr[mid:])

  while left_loca<len(left) and right_loca<len(right):
    if left[left_loca] <= right[right_loca]:
      result.append(right[right_loca])
      right_loca += 1
    else:
      result.append(left[left_loca])
      left_loca += 1
  
  while left_loca<len(left) or right_loca<len(right):
    if left_loca<len(left):
      result.append(left[left_loca])
      left_loca += 1
    elif right_loca<len(right):
      result.append(right[right_loca])
      right_loca += 1
  return result

print("".join(map(str,merge_sort(q))))
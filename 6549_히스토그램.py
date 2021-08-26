import sys

def solves(left,right):
    if left==right:
        return arr[left]

    mid = (left+right)//2
    left_location = mid
    right_location = mid+1
    current_height = min(arr[left_location],arr[right_location])
    max_area = current_height * (right_location-left_location+1)

    while left_location>left or right_location<right:
        if right_location<right and (arr[left_location-1] < arr[right_location+1] or left_location==left):
            right_location += 1
            current_height = min(current_height, arr[right_location])
        else:
            left_location -= 1
            current_height = min(current_height, arr[left_location])
        max_area = max(max_area ,current_height * (right_location-left_location+1))
    
    return max(solves(left,mid),solves(mid+1,right),max_area)



while True:
    arr = list(map(int,sys.stdin.readline().split()))
    right = arr[0]
    if right == 0:
        break
    print(solves(1,right))
    
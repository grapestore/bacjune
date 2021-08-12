import sys


home_num, wifi = map(int,sys.stdin.readline().split())
home_loca = []
for x in range(home_num):
    location = int(input())
    home_loca.append(location)
home_loca.sort()
wifi = wifi - 2
start = home_loca[0]
end = max(home_loca)
result = []
result.append(home_loca[0])
result.append(home_loca[len(home_loca)])
while wifi>0:
    mid = (end - start)//2
    closer_distance = 10000
    for nums in range(home_num):
        if abs(mid - home_loca[nums]) < prev_distance:
            closer_distance = nums
    result.append(home_loca[nums])
    if home_loca[mid]-home_loca[start] > home_loca[end]-home_loca[mid]:
        result.append(home_loca[mid])
        end = mid-1
    else:
        result.append(home_loca[mid])
        start = mid+1
    wifi -= 1

result_max = 1000
for ans in range(len(result)-1):
    for qqq in range(ans+1,len(result)):
        if abs(result[ans] - result[qqq]) < result_max:
            result_max = abs(result[ans] - result[qqq])
        
print(result_max)
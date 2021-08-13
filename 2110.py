import sys


home_num, wifi = map(int,sys.stdin.readline().split())
home_loca = []
for x in range(home_num):
    location = int(input())
    home_loca.append(location)
home_loca.sort()
start = home_loca[0]
left = 1
end = home_loca[-1]-home_loca[0]
result = 0
while left<=end:
    length = (left + end)//2
    count = 1
    start = home_loca[0]
    for i in range(home_num):
        if start + length <= home_loca[i]:
            count += 1
            start = home_loca[i]
    if wifi > count:
        end = length - 1
    elif wifi <= count:
        left = length + 1
        result = length
print(result)
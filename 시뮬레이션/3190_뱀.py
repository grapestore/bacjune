import sys

apple = []
direction_check = []
road = []

long = int(sys.stdin.readline())
apple_num = int(sys.stdin.readline())
apple_loca = [[0]*long for i in range(long)]
for i in range(apple_num):
    lolo = list(map(int,sys.stdin.readline().split()))
    apple_loca[lolo[0]-1][lolo[1]-1] = 1
direc_num = int(sys.stdin.readline())
for j in range(direc_num):
    times, direc = sys.stdin.readline().split()
    direction_check.append([int(times),direc])
direction = 0
x = 1
y = 1
length = 1
count = 0

def direction_solve(direction):
    global count
    if direction_check:
        if direction_check[0][0] == count:
            if direction_check[0][1] == 'D':
                direction += 1
                direction_check.pop(0)
            elif direction_check[0][1] == 'L':
                direction -= 1
                direction_check.pop(0)
            if direction>3:
                direction= 0
            elif direction<0:
                direction = 3
    return direction

while 1<=x<=long and 1<=y<=long:
    
    stable = False
    direction = direction_solve(direction)
    ##right
    if direction == 0:
        x += 1
    ##down
    elif direction == 1:
        y += 1
    #left
    elif direction == 2:
        x -= 1
    #up
    elif direction == 3:
        y -= 1
    while length < len(road):
        road.pop(0)
    if x>long or y>long or x<1 or y<1: count+=1; break
    if [y,x] in road: count+=1; break
    road.append([y,x])
    ## eat apple 
    while apple_loca[y-1][x-1] == 1:
        apple_loca[y-1][x-1] = 0
        count += 1
        stable = True
        length += 1
        if x>long or y>long or x<1 or y<1: count+=1; break
        if [y,x] in road: count+1; break
        road.append([y,x])
    if stable == False:
        count += 1
    
print(count)


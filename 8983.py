import sys



    



def distance_check(gun_num,x,y):
    distance = abs(gun_num-x)+y 
    return distance

if __name__ == '__main__':
    gun_count, ani_num, gun_range = map(int,sys.stdin.readline().split())
    gun_num = list(map(int,sys.stdin.readline().split()))
    animal = []
    for j in range(ani_num):
        temp2 = list(map(int,sys.stdin.readline().split()))
        animal.append(temp2)
    gun_num.sort()
    count = 0
    for x in animal:
        left = 0
        right = len(gun_num)-1
        while left <= right :
            mid = (left+right)//2
            if distance_check(gun_num[mid],x[0],x[1])<=gun_range:
                count+=1
                break
            if x[0] - gun_num[mid] > 0:
                left = mid + 1
            else:
                right = mid -1
    print(count)
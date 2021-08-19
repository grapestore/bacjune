import sys

result = []
arr = []
num = int(sys.stdin.readline())
for x in range(num):
    k = input()
    temp_arr = []
    for y in k:
        temp_arr.append(int(y))
    arr.append(temp_arr)
def divide(n,x_start,x_end,y_start,y_end):
    if n < 2:
        return
    one_count = 0
    zero_count = 0
    temp = '('
    
    for i in range(y_start,y_end):
        for j in range(x_start,x_end):
            if arr[i][j] == 0:
                zero_count += 1
                temp += '0'
            else:
                one_count += 1
                temp += '1'
            
    if one_count == 0 and zero_count>0:
        return 0
    elif one_count >0 and zero_count==0:
        return 1
    elif n==2 and one_count>0 and zero_count>0:
        temp += ')'
        return temp
    if one_count>0 and zero_count>0:
        #print(n,x_start,x_end,y_start,y_end, one_count, zero_count)
        #1사
        one = divide(n//2,x_start,(x_start+x_end)//2,y_start,(y_start+y_end)//2)
        #2사
        two = divide(n//2,(x_start+x_end)//2,x_end,y_start,(y_start+y_end)//2)
        #3사
        three = divide(n//2,x_start,(x_start+x_end)//2,(y_start+y_end)//2,y_end)
        #4사
        four = divide(n//2,(x_start+x_end)//2,x_end,(y_start+y_end)//2,y_end)
    if one and two and three and four == 0 and one and two and three and four == 1:
        return one
    else:
        return f'({one}{two}{three}{four})'


print(divide(num,0,num,0,num))
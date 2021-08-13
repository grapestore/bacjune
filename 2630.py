import sys

def recurs(n,w_start,w_end,h_start,h_end):
    if n < 2:
        return
    global zero_count, one_count
    zero_check = 0
    one_check = 0
    
    for i in range(h_start,h_end):
        for j in range(w_start,w_end):
            if arr[i][j] == 0:
                zero_check += 1
            if arr[i][j] == 1:
                one_check += 1
    if zero_check == 0 and one_check>0:
        one_count += 1
        #print('only 1',w_start,h_start,zero_check,one_check,zero_count,one_count)
    if zero_check > 0 and one_check==0:
        zero_count += 1
        #print('only 0',w_start,h_start,zero_check,one_check,zero_count,one_count)
    if zero_check > 0 and one_check>0 and n == 2:
        one_count += one_check
        zero_count += zero_check
        #print('n = 2',w_start,w_end,h_start,h_end,zero_check,one_check,zero_count,one_count)
    
    if zero_check > 0 and one_check>0:
        recurs(n//2,w_start,(w_start+w_end)//2,h_start,(h_start+h_end)//2)
        recurs(n//2,(w_start+w_end)//2,w_end,h_start,(h_start+h_end)//2)
        recurs(n//2,w_start,(w_start+w_end)//2,(h_start+h_end)//2,h_end)
        recurs(n//2,(w_start+w_end)//2,w_end,(h_start+h_end)//2,h_end)


num = int(sys.stdin.readline())
arr = []
for k in range(num):
    tmp = []
    for x in map(int,sys.stdin.readline().split()):
        tmp.append(x)
    arr.append(tmp)
zero_count = 0
one_count = 0 
recurs(num,0,num,0,num)
print(zero_count)
print(one_count)
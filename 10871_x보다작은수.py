n,check_num = map(int,input().split())
array = input().split()
result_array = []
for x in array:
    result_array.append(int(x))
last_result = []
for check in result_array:
    if check < check_num:
        last_result.append(check)
for x in last_result:
    print(x, end=' ')

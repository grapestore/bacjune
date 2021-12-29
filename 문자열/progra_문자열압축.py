def solution(s):
    answer = 0
    result = []
    for i in range(1,len(s)//2+1):
        last = ''
        temp = s[:i]
        cnt = 1
        for j in range(i,len(s),i):
            if temp == s[j:i+j]:
                cnt+=1
            else:
                if cnt != 1:
                    last = last + str(cnt) + temp
                else:
                    last = last + temp
                cnt = 1
                temp = s[j:i+j]
        if cnt != 1:
            last = last + str(cnt) + temp
        else:
            last = last + temp
        result.append(len(last))
    if len(result)>0:
        return min(result)
    else:
        return 1
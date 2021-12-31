import datetime

def solution(lines):
    time = []
    for x in lines:
        temp = x.split()
        end_temp = temp[0]+" "+temp[1]
        end_day = datetime.datetime.strptime(end_temp, '%Y-%m-%d %H:%M:%S.%f')
        sec = float(temp[2][:-1])
        start_day = end_day - datetime.timedelta(seconds=sec)
        time.append([start_day,end_day])
    answer = 0
    for i in range(len(time)):
        count = 0
        start = time[i][1]
        end = time[i][1] + datetime.timedelta(seconds=0.999)
        for j in range(i,len(time)):
            if start<=time[j][0]<end or start<=time[j][1]<end or (time[j][0]<=start and time[j][1]>=end):
                count += 1
        if count > answer:
            answer = count
        
    return answer
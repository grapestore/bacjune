from collections import defaultdict
import math

def gyo(dict1, dict2):
    check1 = dict1
    check2 = dict2
    arr = []
    for x in dict1:
        if x in check2:
            if check1[x]<check2[x]:
                for _ in range(check1[x]):
                    arr.append(x)
            else:
                for _ in range(check2[x]):
                    arr.append(x)
    return len(arr)
            
def sums(dict1, dict2):
    check1 = dict1
    check2 = dict2
    arr = []
    for x in dict1:
        if check1[x]>check2[x]:
            for _ in range(check1[x]):
                arr.append(x)
        else:
            for _ in range(check2[x]):
                arr.append(x)
    for x in dict2:
        if x not in arr:
            for _ in range(dict2[x]):
                arr.append(x)
    
    return len(arr)

def solution(str1, str2):
    answer = 0
    arr1 = defaultdict(int)
    arr2 = defaultdict(int)
    for i in range(len(str1)-1):
        temp = str1[i:i+2]
        if temp.isalpha():
            arr1[temp.lower()] += 1
            
    for i in range(len(str2)-1):
        temp = str2[i:i+2]
        if temp.isalpha():
            arr2[temp.lower()] += 1

    A = gyo(arr1, arr2)
    B = sums(arr1, arr2)
    if B == 0:
        return 65536
    return math.floor(A/B * 65536)
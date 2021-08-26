import sys

if __name__ == "__main__":

    num = int(sys.stdin.readline())
    arr = list(map(int,sys.stdin.readline().split()))
    result = []
    answer = []
    for i in range(num):
        while result:
            if result[-1][1] > arr[i]:
                answer.append(result[-1][0])
                break
            else:
                result.pop()
        if not result:
            answer.append(0)
        result.append([i+1, arr[i]])
    print(' '.join(map(str,answer)))
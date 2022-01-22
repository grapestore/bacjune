def divide(size,x,y):
    if size == 1:
        if matrix[y][x] == 0:
            answer[0] += 1
        else:
            answer[1] += 1
        return
    zero_count = 0
    one_count = 0
    status = True
    for j in range(y,y+size):
        for i in range(x,x+size):
            if matrix[j][i] == 0:
                zero_count += 1
            else:
                one_count += 1
            if zero_count>0 and one_count>0:
                status = False
                break
        if status == False:
            break
            
    if zero_count == 0:
        answer[1] += 1
        return 
    elif one_count == 0:
        answer[0] += 1
        return 
    
    nextSize = size//2
    #1
    divide(nextSize,x+nextSize*0,y+nextSize*0)
    #2
    divide(nextSize,x+nextSize*1,y+nextSize*0)
    #3
    divide(nextSize,x+nextSize*0,y+nextSize*1)
    #4
    divide(nextSize,x+nextSize*1,y+nextSize*1)
    

def solution(arr):
    global matrix, answer
    matrix = arr
    answer = [0,0]
    divide(len(arr),0,0)
    return answer

if __name__ == "__main__":
  solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]])
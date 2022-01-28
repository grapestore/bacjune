def rotate(matrix):
    global arr1, arr2, arr3
    
    # 90
    arr1 = [[0] * N for _ in range(N)]
    # 180
    arr2 = [[0] * N for _ in range(N)]
    # 270
    arr3 = [[0] * N for _ in range(N)]
    
    for j in range(N):
        for i in range(N):
            arr1[i][N-1-j] = matrix[j][i]
            arr2[N-1-j][N-1-i] = matrix[j][i]
            arr3[N-1-i][j] = matrix[j][i]
    
def check(lock, startx, starty, x):
    check = [x[:] for x in lock]
    for j in range(N):
        for i in range(N):
            check[starty+j][startx+i] += x[j][i]
            
    for i in range(M):
        for j in range(M):
            if check[N+i][N+j] != 1:
                return False;

    return True
    
def solution(key, lock):
    global N,M
    N = len(key)
    M = len(lock)
    rotate(key)
    new_arr = [[0] * (M*2+N) for _ in range(M*2+N)]
    
    for j in range(M):
        for i in range(M):
            new_arr[N+j][N+i] = lock[j][i]
            
    for x in [key,arr1,arr2,arr3]:            
        for j in range(1, M+N):
            for i in range(1, M+N):
                if check(new_arr,i,j,x):
                    return True
    
    return False
if __name__ == "__main__":
  print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
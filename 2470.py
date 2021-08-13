# import sys

# def permutations(ref, n):

#     ans = []
#     if n > len(ref): return ans
#     if n == 1:
#         for item in ref: ans.append([item])
#     elif n>1:
#         for i in range(len(ref)):
#             temp_ref = ref[:]
#             temp_ref.remove(ref[i]) 
#             for p in permutations(temp_ref, n-1):
#                 ans.append([ref[i]]+p)
#     return ans

# num = int(input())
# arr = []
# result = [0,0]
# min_max = 100000
# for x in map(int,sys.stdin.readline().split()):
#     arr.append(x)
# set(arr)
# for arr_check in permutations(arr,2):
#     #print(arr_check, abs(arr_check[0] + arr_check[1]), min_max)
#     if abs(arr_check[0] + arr_check[1]) < min_max:
#         #print(arr_check, abs(arr_check[0] + arr_check[1]), min_max)
#         min_max = abs(arr_check[0] + arr_check[1])
#         result[0] = arr_check[0]
#         result[1] = arr_check[1]
# result.sort()
# print(result)

arr = []

def permutations(ref, n):

    ans = []

    if n > len(ref): return ans



    if n == 1:
        for item in ref: ans.append([item])

    elif n>1:
        for i in range(len(ref)):
            temp_ref = ref[:]
            temp_ref.remove(ref[i]) 
            for p in permutations(temp_ref, n-1):
                ans.append([ref[i]]+p)
    return ans

if __name__ == '__main__':
    temp = permutations(list(range(5)), 3)
    print(temp)
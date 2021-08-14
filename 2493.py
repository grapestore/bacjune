stk = [6, 9, 5, 7, 4]
result = []
for i in reversed(stk):
    for j in reversed(range(len(stk)-1)):
        if i < stk[j]:
            result.append(j+1)
            stk.pop()
            break
        elif i>stk[j] and j ==0:
            result.append(0)
result.append(0)
print(result)
for k in reversed(result):
    print(k, end=' ')
import sys
sys.stdin = open('inputs.text')


n,m = sys.stdin.readline().split()
a = sys.stdin.readline().split()
b = sys.stdin.readline().split()

resultA = len(list(set(a) - set(b)))
resultB = len(list(set(b) - set(a)))
print(resultA + resultB)
import sys
sys.stdin = open('inputs.text')

n,m = sys.stdin.readline().split()
a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))

print(*sorted((a+b)))
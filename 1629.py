import sys


def Mul(a, b):
    # 만약 b가 1이라면 모듈러 연산 결과 반환
    if b == 1:
        return a % C

    remain = Mul(a, b // 2)

    if b % 2 == 0:
        return remain * remain % C

    else:
        return remain * remain * a % C


A, B, C = map(int, sys.stdin.readline().split())

print(Mul(A, B))
import sys

N,M = map(int, sys.stdin.readline().split())
n = []

for i in range(N, M+1):
    if i == 1 :
        continue
    # 에라토스테네스의 체
    for j in range(2,int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        print(i)

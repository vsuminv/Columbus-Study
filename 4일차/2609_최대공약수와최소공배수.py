import sys

a , b = map(int, sys.stdin.readline().split())
N, M = a, b


# 유클리드 호제법 이용
# https://blogshine.tistory.com/112

# M이 0이 되기 전까지 N을 M으로 나눔 (N > M 일때만)
# N을 M으로 나눈 값은 r에 넣고 M 값을 N에 넣고 r 값을 M에 넣어 다시 비교하여 0이 나오기 전까지 반복
while M != 0:
    N = N % M
    N, M = M, N

# 최대공약수
print(N)
# 최소공배수 = 두 자연수 곱 / 최대 공약수
print(a*b//N)


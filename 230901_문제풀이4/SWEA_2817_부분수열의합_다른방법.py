"""
A1, A2, ... , AN의 N개의 자연수가 주어졌을 때,
최소 1개 이상의 수를 선택하여 그 합이 K가 되는 경우의 수를 구하는 프로그램을 작성하시오.

"""


def f(i, N, s, K, rs):  # i 번째 원소, N개의 자연수 수열, s : 만들고있는 부분수열의 합 , K :원하는 부분수열의합 , rs: 남은 원소들의 합
    global cnt
    if i == N:
        if s == K:
            cnt += 1
    elif s > K:
        return
    elif s + rs < K:    # 뒤에 남은 모든 원소를 더해도 K보다 작으면
        return
    else:
        f(i + 1, N, s + A[i], K, rs - A[i])
        f(i + 1, N, s, K, rs - A[i])


T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = 0
    f(0, N, 0, K, sum(A))
    print(f'#{tc} {cnt}')

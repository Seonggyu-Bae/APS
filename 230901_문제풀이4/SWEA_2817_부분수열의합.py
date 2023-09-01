"""
A1, A2, ... , AN의 N개의 자연수가 주어졌을 때,
최소 1개 이상의 수를 선택하여 그 합이 K가 되는 경우의 수를 구하는 프로그램을 작성하시오.

"""
def make_subsequence_sum(n, k):
    cnt = 0  # 합이 K가 되는 경우의 수
    for i in range(1 << N):  # 부분 집합의 개수  1<<N개
        s = 0  # 부분 집합의 합
        for j in range(N):  # j번 비트
            if i & (1 << j):  # i의 j번 비트 검사
                s += A[j]  # 0이 아니면 j번 원소가 부분집합에 포함됨
                if s > k:
                    break
        if s == K:
            cnt += 1
    return cnt


T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    print(f'#{tc}', make_subsequence_sum(N, K))

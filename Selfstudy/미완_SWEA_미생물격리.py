T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())

    sector = [[0] * N for _ in range(N)]

    sector1 = [[()] * N for _ in range(N)]

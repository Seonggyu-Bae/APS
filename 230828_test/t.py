T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v
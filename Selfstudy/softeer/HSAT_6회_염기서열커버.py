import sys

input = sys.stdin.readline
N, M = map(int, input().split())

good = [input().rstrip() for _ in range(N)]

ans = N

for i in range(N):
    for j in range(M):
        for k in range(i + 1, N):
            if good[i][j] == good[k][j] or good[i][j] == '.' or good[k][j] == '.':
                pass
            else:
                break
        else:
            if i == k:
                break
            ans -= 1

print(ans)

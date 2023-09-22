# 서로소 집합 문제인거 같음

def find_set(x):
    if x == parent[x]:
        return x

    # 경로 압축
    parent[x] = find_set(parent[x])
    return parent[x]


def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    parent = [x for x in range(N + 1)]

    info = [list(map(int, input().split())) for _ in range(M)]

    for i in range(M):
        p1, p2 = info[i][0], info[i][1]
        union(p1, p2)
    for i in range(M):
        p1, p2 = info[i][0], info[i][1]
        union(p1, p2)

    ans = len(set(parent)) - 1
    print(f'#{tc} {ans}')

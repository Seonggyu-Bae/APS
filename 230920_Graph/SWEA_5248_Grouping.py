def find_set(x):
    if parent[x] == x:
        return x

    # 경로압축
    parent[x] = find_set(parent[x])
    return parent[x]


def union(x,y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return

    if x<y:
        parent[y] = x
    else:
        parent[x] = y



T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    resume = list(map(int, input().split()))
    parent = [i for i in range(N+1)]

    temp = [] * M
    for i in range(0,M*2,2):
        union(resume[i],resume[i+1])

    for i in range(0,M*2,2):
        union(resume[i],resume[i+1])

    print(f'#{tc} {len(set(parent))-1}')
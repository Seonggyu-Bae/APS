def find_set(x):
    if parent[x] == x :
        return x
    # 경로 최적화
    parent[x] = find_set(parent[x])
    return parent[x]

def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x==y:    # 싸이클 발생
        return

    if x<y:
        parent[y] = x
    else:
        parent[x] = y

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())

    info_list = []
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        info_list.append((n1,n2,w))

    info_list.sort(key=lambda x : x[2])
    parent = [i for i in range(V+1)]

    cnt = 0
    weight_sum = 0
    for s,e,w in info_list:
        if find_set(s) != find_set(e):
            cnt += 1
            weight_sum += w
            union(s,e)

            if cnt == V:
                break

    print(f'#{tc} {weight_sum}')

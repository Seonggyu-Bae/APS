def check(cnt,cost):
    global min_cost
    if cnt==N:
        if min_cost > cost:
            min_cost = cost
        return


    for idx, c in enumerate(V[cnt]):
        if factory[idx] == 1 or cost>min_cost:
            continue
        cost += c
        factory[idx] = 1
        check(cnt+1,cost)
        factory[idx] = 0
        cost -= c

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]
    min_cost = 1500
    factory = [0] * N

    check(0,0)

    print(f'#{tc} {min_cost}')
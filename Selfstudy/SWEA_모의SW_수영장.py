def solve(cnt, cost):
    global ans
    if cnt >= 12:
        if cost < ans:
            ans = cost
        return
    solve(cnt + 1, cost + d * plan[cnt])
    solve(cnt + 1, cost + m)
    solve(cnt + 3, cost + t_m)
    solve(cnt + 12, cost + y)


T = int(input())

for tc in range(1, T + 1):
    d, m, t_m, y = map(int, input().split())
    plan = list(map(int, input().split()))
    ans = 0xfffffff

    solve(0, 0)
    print(f'#{tc} {ans}')

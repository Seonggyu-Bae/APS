def solve(cnt, w, v):
    global ans
    if w > K:
        return
    if v > ans:
        ans = v
    if cnt == N:
        return

    solve(cnt + 1, w + WandV[cnt][0], v + WandV[cnt][1])
    solve(cnt + 1, w, v)


N, K = map(int, input().split())

WandV = [list(map(int, input().split())) for _ in range(N)]
ans = 0
solve(0, 0, 0)
print(ans)

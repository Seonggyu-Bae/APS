def solve(cnt, s):
    global ans

    if cnt == N:
        return

    s += numbers[cnt]
    if s == S:
        ans += 1

    solve(cnt + 1, s - numbers[cnt])
    solve(cnt + 1, s)


N, S = map(int, input().split())
numbers = list(map(int, input().split()))
ans = 0

solve(0, 0)
print(ans)

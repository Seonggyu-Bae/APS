def solve(r,c,val):
    global min_sum
    if r>=N or c>=N:
        return
    if (r,c) == (N-1,N-1):
        val += arr[r][c]
        if val < min_sum:
            min_sum = val
        return
    solve(r,c+1, val+arr[r][c])
    solve(r+1,c,val+arr[r][c])



T = int(input())
for tc in range(1,T+1):
    N= int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    min_sum = 0xfffffff
    solve(0,0,0)
    print(f'#{tc} {min_sum}')
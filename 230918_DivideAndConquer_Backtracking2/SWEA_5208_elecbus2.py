def check(n,where,cnt,now):
    global min_cnt

    if now > where or cnt>=min_cnt:
        return

    if where >= n:
        if min_cnt > cnt:
            min_cnt = cnt
        return

    check(n, now+NandMs[now], cnt+1, now+1)
    check(n, where, cnt, now+1)


T = int(input())

for tc in range(1,T+1):
    NandMs = list(map(int, input().split()))
    min_cnt = NandMs[0]
    N = NandMs[0]
    check(N,1+NandMs[1],0,2)

    print(f'#{tc} {min_cnt}')
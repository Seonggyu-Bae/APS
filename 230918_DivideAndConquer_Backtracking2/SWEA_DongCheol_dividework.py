def find(cnt,temp):
    global lotto
    if cnt == N:
        if temp > lotto:
            lotto = temp
        return

    for idx, probability in enumerate(p[cnt]):
        if work[idx] == 1 or temp <= lotto:
            if cnt!=0:
                continue
        if probability == 0:
            return
        work[idx] = 1
        zero_tmp = 0
        if probability == 0:
            zero_tmp = temp
            temp = 0
        else:
            temp *= probability/100

        find(cnt+1,temp)
        work[idx] = 0
        if probability == 0:
            temp = zero_tmp
        else:
            temp /= probability/100


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    p = [list(map(int, input().split())) for _ in range(N)]
    work = [0] * N
    lotto = 0
    find(0,1)

    print(f'#{tc} {lotto*100:.6f}')
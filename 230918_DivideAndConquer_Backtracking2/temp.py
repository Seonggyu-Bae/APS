def find(cnt,temp):
    global lotto
    if temp <= lotto:   # 백트래킹 조건을 잘 찾고 생각하자
        return
    if cnt == N:
        if temp > lotto:
            lotto = temp
        return

    for idx, probability in enumerate(p[cnt]):
        if probability == 0:    # 이것도 마찬가지임
            continue
        if work[idx] == 1 or temp <= lotto:
            if cnt!=0:
                continue

        work[idx] = 1
        temp *= probability/100
        find(cnt+1,temp)
        work[idx] = 0
        temp /= probability/100


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    p = [list(map(int, input().split())) for _ in range(N)]
    work = [0] * N
    lotto = 0
    find(0,1)

    print(f'#{tc} {lotto*100:.6f}')
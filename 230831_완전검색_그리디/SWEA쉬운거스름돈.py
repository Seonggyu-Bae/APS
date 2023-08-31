
T = int(input())

for tc in range(1, T + 1):
    cnt = [0] * 8
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    N = int(input())
    i = 0

    while N >= 10:
        if N < money[i]:
            i += 1
        else:
            cnt[i] += 1
            N -= money[i]

    print(f'#{tc}')
    print(*cnt)

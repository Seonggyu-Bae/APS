T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N개의 컨테이너, M대의 트럭
    weight = list(map(int, input().split()))  # 각 컨테이너의 무게
    t = list(map(int, input().split()))  # 각 트럭의 적재용량
    weight_total = 0

    t.sort()
    weight.sort()
    j = N - 1

    for i in range(M - 1, -1, -1):
        while j != -1:
            if t[i] >= weight[j]:
                weight_total += weight[j]
                j -= 1
                break
            else:
                j -= 1

    print(f'#{tc} {weight_total}')

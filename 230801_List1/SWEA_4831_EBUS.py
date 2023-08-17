T = int(input())

for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    station_num = list(map(int, input().split()))
    charging_count = 0

    temp = 0
    pos = 0
    is_possible = True
    # 충전기 사이거리가 k 이상이면 불가능함
    for i in range(len(station_num)-1):
        if station_num[0] > K:
            print(f'#{tc} {charging_count}')
            is_possible = False
        if station_num[i+1] - station_num[i] > K:
            print(f'#{tc} {charging_count}')
            is_possible = False
        if not is_possible:
            break
    if not is_possible:
        continue

    # k씩 위치를 증가시키고 그 안에 충전기가 있다면 가장 먼 충전기의 위치로 버스를 이동시킴
    # 충전횟수 증가
    # 위치가 종점보다 멀어지면 종료
    while True:
        temp += K
        if temp >= N:
            break
        for x in station_num:
            if temp >= x:
                pos = x

        charging_count += 1
        temp = pos


    print(f'#{tc} {charging_count}')

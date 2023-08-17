T = int(input())

for tc in range(1,T+1):
    K, N, M = map(int, input().split())
    charger_location = list(map(int,input().split()))

    # 출발지와 도착지를 추가함
    charger_location = [0] + charger_location
    charger_location = charger_location + [N]

    # 각 정류장 확인하면서 지나가고
    # 만약에 내가 이전 정류장에서 충전 안하면 도착을 하지 못하는 정류장이면
    # 이전 충전소에서 충전하기
    last_charger_pos = 0
    charging_count = 0
    for i in range(1, M+2):
        if charger_location[i] - charger_location[i-1] > K: # 정류장 사이가 멀다
            charging_count = 0
            break
        # 아니라면? last_charger_pos + K 올 수 있는 정류장이라면
        # 못올때만 이전 정류장에서 충전(이전 정류장에서 충전 했다고 치자)
        if last_charger_pos + K <charger_location[i]:
            last_charger_pos = charger_location[i-1]
            charging_count += 1

    print(f'{tc} {charging_count}')


def checkcheck(idx, count, n):
    global player
    # 조긴이 위에서 하나라도 맞으면 들어가서 안나오기때문에 다 if로 때려아함.
    if 0 <= cards[idx] - 1 and cards[idx] + 1 < 10:
        if count[cards[idx] - 1] and count[cards[idx]] and count[cards[idx] + 1]:
            player = n
            return
    if cards[idx] + 2 < 10:
        if count[cards[idx]] and count[cards[idx] + 1] and count[cards[idx] + 2]:
            player = n
            return
    if 0 <= cards[idx] - 2:
        if count[cards[idx] - 2] and count[cards[idx] - 1] and count[cards[idx]]:
            player = n
            return
    if count[cards[idx]] >= 3:
        player = n
        return
    else:
        player = 0

T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    # 카드의 개수는 총 12개이며 6개씩 뽑는다
    # (단, 순서대로 뽑아나가다가 run/triplet 이 먼저 나오면 끝이 난다)
    # 카드에 적힌 숫자는 0~9이다
    count_1 = [0] * 10
    count_2 = [0] * 10
    player = 0

    for i in range(0, 12, 2):
        count_1[cards[i]] += 1
        if i >= 4:
            checkcheck(i, count_1, 1)
        if player == 1:
            print(f'#{tc} {player}')
            break
        count_2[cards[i+1]] += 1
        if i >= 4:
            checkcheck(i+1, count_2, 2)
        if player == 2:
            print(f'#{tc} {player}')
            break
    else:
        print(f'#{tc} {player}')
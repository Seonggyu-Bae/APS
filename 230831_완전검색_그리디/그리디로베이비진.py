def check_rt(player_cards):
    for i in range(10):
        if i < 8 and player_cards[i] and player_cards[i + 1] and player_cards[i + 2]:
            return True
        if player_cards[i] >= 3:
            return True
    return False


# 0부터 9까지 카드가 몇장있는지 표시하는 배열을 이용해서 Run or Triplet 검사
T = int(input())
for tc in range(1, T + 1):
    cards = list(map(int, input().split()))
    p1 = [0] * 10
    p2 = [0] * 10
    winner = 0
    for i in range(0, 12, 2):
        p1[cards[i]] += 1
        if check_rt(p1):
            winner = 1
            break
        p2[cards[i + 1]] += 1
        if check_rt(p2):
            winner = 2
            break

    print(f'#{tc} {winner}')

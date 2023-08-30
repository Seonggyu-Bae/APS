T = int(input())

for tc in range(1, T + 1):
    card = list(map(int, input().split()))

    player1 = []
    player2 = []
    cnt1 = [0] * 10
    cnt2 = [0] * 10
    winner = 0

    for i in range(0, len(card), 2):
        player1.append(card[i])
        player2.append(card[i + 1])
        cnt1[card[i]] += 1
        cnt2[card[i + 1]] += 1

        card_cnt = len(player1)
        if card_cnt > 2:
            player1.sort()
            for j in range(card_cnt - 2):
                if player1[j] == player1[j + 1] == player1[j + 2]:
                    winner = 1
                    break
                for k in range(8):
                    if cnt1[k] and cnt1[k + 1] and cnt1[k + 2]:
                        winner = 1
                        break
            if winner == 1:
                break

        card_cnt_2 = len(player2)
        if card_cnt_2 > 2:
            player2.sort()
            for j in range(card_cnt_2 - 2):
                if player2[j] == player2[j + 1] == player2[j + 2]:
                    winner = 2
                for k in range(8):
                    if cnt2[k] and cnt2[k + 1] and cnt2[k + 2]:
                        winner = 2
            if winner != 0:
                break
        if winner != 0:
            break

    print(f'#{tc} {winner}')

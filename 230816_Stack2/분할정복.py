def solve(start, end):
    if start == end:
        return start
    mid = (start + end) // 2
    win1 = solve(start, mid)
    win2 = solve(mid + 1, end)

    if card[win1] == card[win2]:
        return win1

    elif card[win1] == 1:
        if card[win2] == 2:
            return win2
        else:
            return win1

    elif card[win1] == 2:
        if card[win2] == 1:
            return win1
        else:
            return win2

    elif card[win1] == 3:
        if card[win2] == 1:
            return win2
        else:
            return win1
    return


T = int(input())

for tc in range(1,T+1):
    N = int(input())

    card = list(map(int,(input().split())))
    end = len(card)-1

    print(f'#{tc} {solve(0,end)+1}')


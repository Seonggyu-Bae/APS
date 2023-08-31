def check_rt(cards):
    if cards[0] == cards[1] == cards[2]:
        return True
    if cards[0] == cards[1] + 1 == cards[2] + 2:
        return True
    return False


# 카드의 순열을 만드는 함수
def make_perm(perm, origin, used, idx):
    # 순열을 만들고 나서 여기서 check_rt()를 호출할거임
    if idx == len(origin):
        return check_rt(perm)
    for i in range(len(origin)):
        if not used[i]:
            perm[idx] = origin[i]
            used[i] = 1
            if make_perm(perm, origin, used, idx + 1):
                # check_rt(perm)이 True 반환되면 베이비진이니까
                return True
            used[i] = 0
    else:  # 한번도 break가 안되었으면 베이비진이 아니니까
        return False


# 교환을 통한 순열 만들기
# idx 번째 요소를 본인 포함(자리 안바꾸는거) 뒤쪽요소와 자리 바꿔보기
# 이게 더 효율적?
def make_perm2(idx, origin):
    if idx == len(origin):
        return check_rt(origin)

    for i in range(idx, len(origin)):
        origin[idx], origin[i] = origin[i], origin[idx]
        if make_perm2(idx + 1, origin):
            return True
        # 자리 다시 돌려놓기
        origin[idx], origin[i] = origin[i], origin[idx]
    else:
        return False


T = int(input())
for tc in range(1, T + 1):
    cards = list(map(int, input().split()))
    p1 = [cards[0], cards[2]]
    p2 = [cards[1], cards[3]]
    winner = 0
    for i in range(4, 12):
        if i % 2 == 0:
            p1.append(cards[i])
            perm = [None] * len(p1)
            used = [0] * len(p1)
            idx = 0
            if make_perm2(0, p1):
                winner = 1
                break

            # if make_perm(perm, p1, used, idx):
            # winner = 1
            # break
        else:
            p2.append(cards[i])
            perm = [None] * len(p2)
            used = [0] * len(p2)
            idx = 0
            if make_perm2(0, p2):
                winner = 2
                break
            # if make_perm(perm, p2, used, idx):
            # winner = 2
            # break
    print(f'#{tc} {winner}')

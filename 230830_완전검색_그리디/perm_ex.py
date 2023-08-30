def perm(i, N):
    if i == N:  # 순열 완성
        print(p)
        return
    else:  # card[i]에 들어갈 숫자를 결정
        for j in range(N):
            if used[j] == 0:  # 아직 사용되기 전이면
                p[i] = card[j]
                used[j] = 1
                perm(i + 1, N)
                used[j] = 0


card = list(map(int, input()))
p = [0] * len(card)
used = [0] * len(card)  # 이미 사용한 카드인지 확인하는

perm(0,len(card))
def perm(i, N, K):  # i: 이전까지 고른 개수, N개에서 K개를 고르는 순열
    global cnt
    cnt += 1
    if i == K:  # 순열 완성 : K개를 모두 고른 경우
        cnt += 1
        print(p)
        return
    else:  # P[i]에 들어갈 숫자를 결정
        for j in range(N):
            if used[j] == 0:  # 아직 사용되기 전이면
                p[i] = card[j]
                used[j] = 1
                perm(i + 1, N, K)
                used[j] = 0


card = [1, 2, 3, 4, 5]
N = len(card)
K = 3  # N개의 숫자에서 K개를 골라 만드는 순열
p = [0] * K
used = [0] * len(card)  # 이미 사용한 카드인지 확인하는
cnt = 0
perm(0, N, K)
print(cnt)
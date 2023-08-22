def postorder(p, N):
    if p <= N//2+1:
        postorder(p * 2, N)
        postorder(p * 2 + 1, N)
        if p * 2 <= N and p * 2 + 1 <= N:
            CBT[p] = CBT[p * 2] + CBT[p * 2 + 1]
        elif p * 2 <= N:
            CBT[p] = CBT[p * 2]
        else:
            CBT[p] = CBT[p]


T = int(input())

for tc in range(1, T + 1):
    N, M, L = map(int, input().split())

    CBT = [0] * (N + 1)

    for _ in range(M):
        leaf, number = map(int, input().split())
        CBT[leaf] = number

    postorder(1, N)
    print(f'#{tc} {CBT[L]}')

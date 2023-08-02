A = [x for x in range(1,14)]
ans = 0
T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    temp = 0
    count = 0
    for i in range(13):
        temp = A[i]
        count = 1
        for j in range(13):
            if count == N and temp == K:
                ans += 1
            if i == j:
                continue
            temp += A[j]
            count += 1


    print(f'#{tc} {ans}')
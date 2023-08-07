A = [x for x in range(1, 13)]
n = len(A)

T = int(input())

for tc in range(1, T + 1):
    ans = 0
    N, K = map(int, input().split())
    for i in range(1 << n):  # 1<<n : 부분 집합의 개수
        temp_sum = 0
        temp_count = 0
        for j in range(n):  # 원소의 수만큼 비트를 비교함
            if i & (1 << j):  # i의 j번 비트가 1인경우
                temp_sum += A[j]  # j번 원소 출력
                temp_count += 1
                if temp_sum > K or temp_count > N:
                    break
        if temp_sum == K and temp_count == N:
            ans += 1

    print(f'#{tc} {ans}')

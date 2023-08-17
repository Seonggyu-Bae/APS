T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    N_number = list(map(int, input().split()))

    for i in range(M):                      # M번 반복
        N_number.append(N_number.pop(0))    # 첫번째 원소를 빼고 맨 뒤로 보냄

    print(f'#{tc} {N_number[0]}')

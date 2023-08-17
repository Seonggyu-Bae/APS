T = int(input())

for tc in range(1, T + 1):
    max_kill = 0  # 최대로 죽일 수 있는 파리수
    N, M = map(int, input().split())  # M == MXM 파리채
    fly_matrix = [list(map(int, input().split())) for _ in range(N)]  # 각 격자안에 파리가 몇마리 있는지 나타내는 배열

    # 파리채 크기를 생각해서 반복 횟수 설정
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            temp_kill = 0
            # 기준점에서 부터 파리채 크기만큼 파리를 잡자
            for k in range(i, i + M):
                for t in range(j, j + M):
                    temp_kill += fly_matrix[k][t]

            if temp_kill > max_kill:
                max_kill = temp_kill

    print(f'#{tc} {max_kill}')

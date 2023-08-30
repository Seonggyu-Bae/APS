def perm(i, N):
    if i == N:  # 순열 완성
        m_dir.append(p[:])
    else:  # s[i]에 들어갈 숫자를 결정
        for j in range(N):
            if used[j] == 0:  # 아직 사용되기 전이면
                p[i] = s[j]
                used[j] = 1
                perm(i + 1, N)
                used[j] = 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    sector = [list(map(int, input().split())) for _ in range(N)]
    min_v = 10000
    m_dir = []                          # 생성된 순열을 저장할 배열

    s = [x for x in range(2, N + 1)]    # 사무실(1) 을 제외하고 순열을 만들려고 생각함
    p = [0] * len(s)
    used = [0] * len(s)

    perm(0, len(s))

    a = len(m_dir)      # 생성된 순열 만큼 반복
    for i in range(a):
        temp = sector[0][m_dir[i][0] - 1]   # 앞뒤로 1이 있으니까 그냥 계산해줌
        for j in range(N - 2):              # 앞뒤로는 따로 계산해주니까 생성된 순열의 마지막 전 원소까지만 보면됨
            temp += sector[m_dir[i][j] - 1][m_dir[i][j + 1] - 1]
        temp += sector[m_dir[i][N - 2] - 1][0]  # 앞뒤로 1이 있으니까 그냥 계산해줌

        if temp < min_v:
            min_v = temp

    print(f'#{tc} {min_v}')

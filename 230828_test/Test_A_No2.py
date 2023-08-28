# 각 기지국은 육각형으로 인접해 있고
# 기지국이 커버하는 사람수가 있음
# 기지국 4개를 설치하는데 사람수 가장 많게 해야함 이득이 각 기지국 사람수를 더한거에 제곱임 (a+b+c+d)^2
# 각 기지국들은 적어도 하나의 기지국과 인접해야함

# BFS + DFS로 구현? 할줄모름
# 무지성 for + 델타

# 기지국의 좌표를 i,j라 할때 j에 따라 주변좌표가 달라진다.
# j가 짝수일때
di = [-1, -1, -1, 0, 0, 1]
dj = [0, -1, 1, -1, 1, 0]

# j가 홀수일때
ddi = [-1, 0, 0, 1, 1, 1]
ddj = [0, -1, 1, -1, 0, 1]

T = int(input())

for tc in range(1, T + 1):
    W, H = map(int, input().split())
    cost_benefit = 0
    cell = [(list(map(int, input().split()))) for _ in range(H)]    # 각 기지국 마다의 사람수

    for i in range(H):
        for j in range(W):
            first, second, third = 0, 0, 0  # 단순 델타로는 첫 기지국 주변에만 있는거 탐색 못함 ex(Y자)
            for k in range(6):
                if j % 2 == 0:
                    a, b = i + di[k], j + dj[k]
                else:
                    a, b = i + ddi[k], j + ddj[k]
                if 0 <= a < H and 0 <= b < W:
                    if cell[a][b] > first:
                        third = second
                        second = first
                        first = cell[a][b]
                    elif cell[a][b] > second:
                        third = second
                        second = cell[a][b]
                    elif cell[a][b] > third:
                        third = cell[a][b]

            temp = (cell[i][j] + first + second + third) ** 2   # 그래서 첫 기지국 주변의 큰 3놈을 고르고
            if temp > cost_benefit:                             # 앞에서 계산한거 보다 크면 넣어줌
                cost_benefit = temp

            for k in range(6):
                if j % 2 == 0:
                    ni, nj = i + di[k], j + dj[k]
                else:
                    ni, nj = i + ddi[k], j + ddj[k]
                if 0 <= ni < H and 0 <= nj < W:
                    for l in range(6):
                        if nj % 2 == 0:
                            nni, nnj = ni + di[l], nj + dj[l]
                        else:
                            nni, nnj = ni + ddi[l], nj + ddj[l]

                        if 0 <= nni < H and 0 <= nnj < W and (nni, nnj) != (i, j):  # 3번째 기지국 정할때는 앞에 갔던걸 다시 갈 위험이 생김 (2번째에서 주변을 탐색하기 때문)
                            for n in range(6):
                                if nnj % 2 == 0:
                                    nnni, nnnj = nni + di[n], nnj + dj[n]
                                else:
                                    nnni, nnnj = nni + ddi[n], nnj + ddj[n]

                                if 0 <= nnni < H and 0 <= nnnj < W and \
                                        (nnni, nnnj) != (i, j) and (nnni, nnnj) != (ni, nj):        # 얘도 마찬가지로 앞에 갔던거 다시 갈 위험이있어서 조건을 줌
                                    cost = (cell[i][j] + cell[ni][nj] + cell[nni][nnj] + cell[nnni][nnnj]) ** 2
                                    if cost > cost_benefit:
                                        cost_benefit = cost

    print(f'#{tc} {cost_benefit}')

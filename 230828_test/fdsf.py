# j짝수
di = [-1, -1, -1, 0, 0, 1]
dj = [0, -1, 1, -1, 1, 0]

# j 홀수
ddi = [-1, 0, 0, 1, 1, 1]
ddj = [0, -1, 1, -1, 0, 1]

T = int(input())


for tc in range(1, T + 1):
    W, H = map(int, input().split())
    cost_benefit = 0
    cell = [(list(map(int, input().split()))) for _ in range(H)]

    for i in range(H):
        for j in range(W):
            first, second, third = 0, 0, 0
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
            cost_benefit = (cell[i][j] + first + second + third) ** 2
            print(cost_benefit,i,j)

            for k in range(6):
                print(i,j)
                if j % 2 == 0:
                    ni, nj = i + di[k], j + dj[k]
                else:
                    ni, nj = i + ddi[k], j + ddj[k]
                    for l in range(6):
                        if nj % 2 == 0:
                            nni, nnj = ni + di[l], nj + dj[l]
                        else:
                            nni, nnj = ni + ddi[l], nj + ddj[l]
                        if 0 <= nni < H and 0 <= nnj < W:  # 수정된 부분
                            for n in range(6):
                                if nnj % 2 == 0:
                                    nnni, nnnj = nni + di[n], nnj + dj[n]
                                else:
                                    nnni, nnnj = nni + ddi[n], nnj + ddj[n]

                                if 0 <= nnni < H and 0 <= nnnj < W and \
                                        (nnni, nnnj) != (i, j) and (nnni, nnnj) != (ni, nj):
                                    cost = (cell[i][j] + cell[ni][nj] + cell[nni][nnj] + cell[nnni][nnnj]) ** 2
                                    if cost > cost_benefit:
                                        cost_benefit = cost

    print(f'#{tc} {cost_benefit}')

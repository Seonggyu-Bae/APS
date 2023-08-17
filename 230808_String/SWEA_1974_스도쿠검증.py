T = int(input())

for tc in range(1,T+1):
    puzzle = [list(map(int, input().split())) for _ in range(9)]
    is_true = 1

    # 행,열 검색
    for i in range(9):
        row_count = [0] * 10
        col_count = [0] * 10
        # 행렬 검색
        for j in range(9):
            row_count[puzzle[i][j]] += 1
            col_count[puzzle[j][i]] += 1
            if row_count[puzzle[i][j]] > 1 or col_count[puzzle[j][i]]  > 1:
                is_true = 0
                break
        if not is_true:
            break

    # 3 X 3
    if is_true:
        for i in range(0,9,3):
            for j in range(0,9,3):
                row_count = [0] * 10
                for x in range(i,i+3):
                    for y in range(j, j+3):
                        row_count[puzzle[x][y]] += 1
                        if row_count[puzzle[x][y]] > 1:
                            is_true = 0
                            break
                    if not is_true:
                        break
                if not is_true:
                    break
            if not is_true:
                break


    print(f'#{tc} {is_true}')
N = 5
arr = [[0]* N for _ in range(N)]



    for i in range(row +1):
        if i == 0:
            arr[row][i] = 1
            continue
        arr[row][i] = arr[row-1][i] + arr[row-1][i-1]



    solve(row+1)

solve(0)

for row in arr:
    print(*row)
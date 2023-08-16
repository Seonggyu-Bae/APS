# N-Queen
# N X N 판에 N개의 퀸을 놓을 수 있는가?
# 한 행에 하나의 퀸을 놓아보기
# 만약 모든 행에 퀸을 다 놓았다면 N개의 퀸을 놓은거니 해를 찾음!

N = int(input())
def solve(row):
    global cnt
    if row == N:    # 모든 행에 퀸을 놓음!
        print('find!')
        cnt += 1
        return

    # row행에 모든 열에 퀸 놓아보기
    for col in range(N):
        # row, col 에 놓을 수 있으면 퀸 놓아보기
        if not col_check[col] and not dia_check1[row+col] and not dia_check2[N-1 + row - col]:
            col_check[col] += 1
            dia_check1[row+col] += 1
            dia_check2[N-1 + row - col] += 1
            solve(row + 1)
            col_check[col] -= 1
            dia_check1[row + col] -= 1
            dia_check2[N - 1 + row - col] -= 1
            # 퀸에 영향을 받으면 1을 더해주고 다음시도를 할 때 1을 빼주면됨

cnt = 0
# 열 사용 가능여부 표시하는 배열 생성
col_check = [0] * N     # 0이면 해당 열에 퀸 없음
# 대각선 사용 가능여부 표시 배열 N X N 배열에서 대각선은 2N-1개
dia_check1 = [0] * (2*N-1) # 좌상에서 우하로 r+c
dia_check2 = [0] * (2*N-1) # 우상에서 좌하로 (N-1) + (r-c)

solve(0)
print(cnt)
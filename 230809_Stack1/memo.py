def pascal(n,num_box):
    # 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성
    for i in range(1,n):        # 두번째 줄부터 N번째 줄까지
        for j in range(i+1):    # 0부터 i번 (i가 2라면 num_box[2][0], 21, 22 만들기 가능)
            if j-1 >= 0:        # 윗 행에 좌우가 존재하면
                num_box[i][j] = (num_box[i-1][j-1] + num_box[i-1][j])
            else:               # 아니면
                num_box[i][j] = num_box[i - 1][j]


T = int(input())

for tc in range(1,T+1):
    # 크기가 N인 파스칼의 삼각형을 만들어야 함
    N = int(input())
    # NXN 크기의 2차원 배열을 만들어서 해보려고 했음
    num_box = [[0] * N for _ in range(N)]
    # 첫번째 줄은 항상 숫자 1이라고 문제에서 주어짐
    num_box[0][0] = 1

    pascal(N,num_box)

    # 출력
    print(f'#{tc}')
    for i in range(0,N):
        for j in range(i+1):
            print(num_box[i][j],end=' ')
        print()
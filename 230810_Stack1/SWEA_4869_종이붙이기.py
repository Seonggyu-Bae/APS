def paper(N):
    my_paper = [0] * (N+1)
    my_paper[1] = 1
    my_paper[2] = 3

    # 이런문제는 규칙을 잘 찾아야한다
    for i in range(3, N + 1):
        my_paper[i] = my_paper[i-1] + my_paper[i-2] * 2

    return my_paper[N]


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    print(f'#{tc} {paper(N//10)}')



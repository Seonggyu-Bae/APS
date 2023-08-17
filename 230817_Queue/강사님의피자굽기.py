T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N: 화덕 자리 M: 피자개수
    # 각 피자의 치즈양
    ci = list(map(int, input().split()))

    # 화덕
    queue = []

    # 최초화덕에는 N개의 피자가 들어감
    for i in range(N):
        queue.append((ci[i], i))

    # 다음에 몇번 피자가 들어가야 하는지 알려주는 변수가 필요
    next = N

    # 아래 작업을 화덕에 피자가 1개가 남았을때 까지 반복
    while len(queue) > 1:
        # 화덕에 제일 먼저 넣은 피자의 치즈 양 확인
        cheese, idx = queue.pop(0)
        # 한바퀴 돌아왔으니 치즈의 양 절반으로 줄여줌
        cheese //= 2
        if cheese > 0:  # 치즈가 남았으니 다시 화덕에 넣어줌
            queue.append((cheese, idx))
        else:           # 치즈가 다 녹았음(0) 다음 피자를 화덕에 넣어주면 된다.
            if next < M:
                queue.append((ci[next], next))
                next += 1

    # 마지막 남은 피자 꺼내서 확인
    last = queue.pop(0)
    print(f'#{tc} {last[1]+1}')
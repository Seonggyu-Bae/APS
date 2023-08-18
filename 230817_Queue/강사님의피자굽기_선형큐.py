T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N: 화덕 자리 M: 피자개수
    # 각 피자의 치즈양
    ci = list(map(int, input().split()))

    # 화덕 선형큐로 구현
    queue = [None] * 10000
    front = rear = -1

    for i in range(N):
        rear += 1
        queue[rear] = (ci[i],i)

    next = N

    while rear - front > 1:
        front += 1
        cheese, num = queue[front]

        cheese //= 2
        if cheese > 0:
            rear += 1
            queue[rear] = (cheese, num)
        else:
            if next < M:
                rear += 1
                queue[rear] = (ci[next], next)
                next += 1

    front += 1
    last = queue[front]
    print(f'#{tc} {last[1] + 1}')
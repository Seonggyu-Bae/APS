for _ in range(10):
    tc = int(input())
    password = list(map(int, input().split()))

    while password[7] != 0:         # 결국 마지막 수가 0이면 끝난거임
        for i in range(1, 6):       # i(1~5)번째수를 i만큼 감소시켜야 함
            password[0] -= i
            if password[0] <= 0:    # 감소시킨 값이 0보다 같거나 작으면
                password[0] = 0     # 0이고
                password.append(password.pop(0))    # 0을 제일 뒤로 보내줌
                break
            else:                   # 감소시킨 값이 0보다 크면 뒤로 보내주고 계속 반복 돌아감
                password.append(password.pop(0))

    print(f'#{tc}', *password)
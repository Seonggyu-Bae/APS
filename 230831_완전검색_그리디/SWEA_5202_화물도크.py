T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    count = 1
    app_form = []

    for i in range(N):
        s, e = map(int, input().split())
        app_form.append([s, e])

    app_form.sort(key=lambda x: x[1])
    end = app_form[0][1]
    for i in range(1, N):
        if app_form[i][0] >= end:
            count += 1
            end = app_form[i][1]

    print(f'#{tc} {count}')
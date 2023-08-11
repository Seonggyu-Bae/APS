# f(N) = f(N-2) * 2 + f(N-1)

def solve(N):
    if N == 20:
        return 3
    elif N == 10:
        return 1
    return solve(N - 20) * 2 + solve(N - 10)


def solve1(N):
    N = N // 10
    counts = [0] * (N + 1)
    counts[1] = 1
    counts[2] = 3

    for i in range(3, N + 1):
        counts[i] = counts[i - 2] * 2 + counts[i - 1]

    return counts[N]


def solve3(length, N):
    # 현재 길이에 가능한 방법을 다 해봅시다.
    # 현재 길이가 찾는 길이와 같다면 count 증가 후 종이 붙이기 중단
    # 현재 길이가 찾는 길이보다 더 길면 끝
    global count

    if length == N:
        count += 1
        return
    elif length > N:
        return
    else:  # 아직 짧다 ( 종이를 덜 붙임 ) 붙여볼 수 있는거 다 붙여보기
        solve3(length + 10, N)
        solve3(length + 20, N)
        solve3(length + 20, N)


def solve3_1(length, N):
    # 현재 길이에 가능한 방법을 다 해봅시다.
    # 현재 길이가 찾는 길이보다 더 길면 끝

    if length == N:
        return 1
    elif length > N:
        return 0
    else:  # 아직 짧다 ( 종이를 덜 붙임 ) 붙여볼 수 있는거 다 붙여보기
        return solve3_1(length + 10, N) + 2 * solve3_1(length + 20, N)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    count = 0
    result = solve(N)
    print(f'#{tc} {solve1(N)}')
    solve3(0, N)
    print(f'#{tc} {count}')

    print(f'#{tc} {solve3_1(0, N)}')

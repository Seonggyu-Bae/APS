'''
1. 문제 해석
    - 문제에서 원하는 목표 -> 명확하게 문제를 파악

2. 어떤 알고리즘을 사용할 것 인가

'''


def recur(level, acc_height):
    global ans

    # 가지치기
    # 현재까지 탑이 선반 높이를 넘어간다면
    # 앞으로는 더 볼 필요가 없다.
    if acc_height >= B:
        ans = min(ans, acc_height)
        return

    # 기저 조건
    if level == N:
        return

        # 해당 점원을 탑에 쓸 경우
    recur(level + 1, acc_height + H[level])
    # 안쓸 경우
    recur(level + 1, acc_height)


T = int(input())

for tc in range(1, T + 1):
    # N명의 점원, 선반의 높이 B
    N, B = map(int, input().split())

    # 점원의 키 H
    H = list(map(int, input().split()))

    ans = int(1e9)  # 최소값 저장
    recur(0, 0)

    print(f'#{tc} {abs(ans - B)}')

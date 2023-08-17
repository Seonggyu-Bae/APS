import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1, 11):
    N = int(input())
    height = list(map(int, input().split()))
    view_sum = 0  # 조망권 확보된 세대수를 저장하는 변수

    for i in range(2, (N - 2)):
        high = 0

        # i번째를 제외한 i-2번째에서 i+2번째까지 빌딩 중 가장 높은 빌딩 구하는 반복문
        for idx in range(i - 2, i + 3):
            if idx == i:
                continue
            if high < height[idx]:
                high = height[idx]

        view = height[i] - high
        # i번째 보다 높은 건물이 없으면 조망권이 생기는 세대가 있음
        if view > 0:
            view_sum += view

    print(f'#{test_case} {view_sum}')
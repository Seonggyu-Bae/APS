# import sys

# sys.stdin = open("input.txt", "r")

for test_case in range(1, 11):
    N = int(input())
    height = list(map(int, input().split()))
    view_sum = 0
    for i in range(2, (N-2)):
        high = 0
        high2 = 0
        for idx in range(i-2, i+3):
            if high < height[idx]:
                high = height[idx]

        for idx in range(i-2, i+3):
            if idx == i:
                continue
            if high < height[idx]:
                high = height[idx]

        if high == height[i]:
            view_sum += high - high2

    print(f'#{test_case} {view_sum}')



"""
N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.
M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.

첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
다음 줄부터 테스트케이스의 첫 줄에 정수의 개수 N과 구간의 개수 M 주어진다. ( 10 ≤ N ≤ 100,  2 ≤ M ＜ N )
다음 줄에 N개의 정수 ai가 주어진다. ( 1 ≤ a ≤ 10000 )

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
"""
import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, (input().split()))
    numbers = list(map(int, input().split()))

    temp_sum = 0
    #첫번째 구간합 구하기
    for i in range(0, M):
        temp_sum += numbers[i]

    min_sum = temp_sum
    max_sum = temp_sum

    #이후에는 전의 구간합에서 가장 앞부분을 빼고 그 다음 수를 더하면 된다.
    for i in range(1, N - M + 1):
        temp_sum -= numbers[i-1]
        temp_sum += numbers[i+M-1]

        # 전에 저장된 값보다 크거나 작으면 저장합시다
        if min_sum > temp_sum:
            min_sum = temp_sum
        if max_sum < temp_sum:
            max_sum = temp_sum

    print(f'#{test_case} {max_sum - min_sum}')

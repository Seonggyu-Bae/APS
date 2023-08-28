"""
참고
N개 원소를 가진 1차원 배열을 3개의 영역으로 나누기
조건: 각 영역은 최소 1개 이상의 원소를 가짐
0 ~i
i+1 ~ j
j+1 ~N-1

"""
T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # 수확한 당근의 개수

    carrot_size = list(map(int, input().split()))

    carrot_size.sort()  # 당근을 크기순으로 정렬
    min_v = 1000  # 포장별 최소 개수 차이, 포장이 불가능한 경우 -1 출력

    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            if carrot_size[i] != carrot_size[i + 1] and carrot_size[j] != carrot_size[j + 1]:  # 같은 크기 사이에 경계를 두면안됨

                small = i + 1  # 소 상자에 들어간 당근 개수
                mid = j - i  # 중 상자에 들어간 당근 개수
                large = N - 1 - j  # 대 상자에 들어간 당근 개수
                print(i, j, small,mid, large)
                if small <= N // 2 and mid <= N // 2 and large <= N // 2:
                    if min_v > (max(small, mid, large) - min(small, mid, large)):
                        min_v = (max(small, mid, large) - min(small, mid, large))

    if min_v == 1000:
        print(f'{tc} -1')
    else:
        print(f'{tc} {min_v}')

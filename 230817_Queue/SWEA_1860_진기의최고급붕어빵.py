T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())  # M초에 K개의 붕어빵 만들기가능
    t = list(map(int, input().split()))
    t.sort()                            # 사람이 오는 시간이 뒤죽박죽이어서 정렬해줌
    is_possible = 1                     # 가능한지 아닌지 기록할 변수

    for i in range(N):
        how_many = t[i] // M * K        # i번째 사람이 오는 시간동안 몇개를 만들수 있는지
        for j in range(0, i + 1):       # 1번째부터 i 번째 사람까지 1개씩 빼보고
            how_many -= 1
            if how_many < 0:            # 0보다 작아지면 붕어빵을 제공할 수 없는 것임
                is_possible = 0         # 변수를 바꿔놓고 for 문을 끝내면 된다.
                break

    if is_possible:
        print(f'#{tc} Possible')
    else:
        print(f'#{tc} Impossible')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    # 버스가 다니는 노선 카운팅 하는 리스트
    st = [0] * 5001

    for _ in range(N):
        a, b = map(int, input().split())
        # a에서 b까지 카운트 해줌
        for i in range(a, b + 1):
            st[i] += 1

    P = int(input())  # P 개의 정류장에 대해 각 정류장에 몇개의 버스 노선이 다니는지

    count = [0] * P
    print(f'#{tc}', end=' ')
    # 정류장 번호(C) 를 받아 그 정류장을 지나는 버스가 몇대인지 st[C] 에서 읽어 출력
    for i in range(P):
        C = int(input())
        print(f'{st[C]}', end=' ')

    print()

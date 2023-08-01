T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # 버스가 다니는 노선 카운팅 하는 리스트
    st = [0] * 5001

    for _ in range(N):
        a,b = map(int, input().split())
        # a에서 b까지 카운트 해줌
        for i in range(a,b+1):
            st[i] += 1

    P = int(input())

    count = [0] * P

    #정류장 번호를 받아 그 정류장을 지나는 버스가 몇대인지 st에서 받아와서 저장
    for i in range(P):
        C = int(input())
        count[i] = str(st[C])

    #출력형식을 맞추기 위해 join사용
    result = ' '.join(count)


    print(f'#{tc} {result} ')
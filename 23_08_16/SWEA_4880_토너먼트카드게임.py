def solve(start, end):
    if start == end:  # 종료조건(각 각 한명이 되면)
        return start    # 인덱스가 반환되는거임 win1이나 win2로 할당됨

    # 분할정복을 이용한다
    mid = (start + end) // 2
    win1 = solve(start, mid)  # 왼쪽의 승자 인덱스
    win2 = solve(mid + 1, end)  # 오른쪽의 승자 인덱스

    # 가위바위보 조건 1: 가위, 2: 바위, 3: 보
    # 같은패라면 번호(인덱스)가 작은 학생이 승자
    if card[win1] == card[win2]:
        return win1

    elif card[win1] == 1:
        if card[win2] == 2:
            return win2
        else:
            return win1

    elif card[win1] == 2:
        if card[win2] == 1:
            return win1
        else:
            return win2

    elif card[win1] == 3:
        if card[win2] == 1:
            return win2
        else:
            return win1
    return


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    card = list(map(int, (input().split())))
    end = len(card) - 1

    # 인덱스는 0부터 시작이지만 학생 번호는 1부터 시작하니까 solve() 결과에 1을 더해서 출력
    print(f'#{tc} {solve(0, end) + 1}')

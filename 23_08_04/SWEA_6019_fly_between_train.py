T = int(input())

for tc in range(1, T + 1):
    # D: 두 기차 사이의 거리
    # A: 기차 A의 속력
    # B: 기차 B의 속력
    # F: 파리의 속력
    D, A, B, F = map(int, input().split())
    # 정답과의 절대오차나 상대오차가 10^-6이하이면 정답임으로 소숫점 6째자리까지
    fly_move_len = format(D / (A+B) * F, ".6f")
    print(f'#{tc} {fly_move_len} ')

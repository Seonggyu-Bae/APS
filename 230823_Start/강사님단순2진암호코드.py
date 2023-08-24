code_dic = {
    (3, 2, 1, 1): 0,
    (2, 2, 2, 1): 1,
    (2, 1, 2, 2): 2,
    (1, 4, 1, 1): 3,
    (1, 1, 3, 2): 4,
    (1, 2, 3, 1): 5,
    (1, 1, 1, 4): 6,
    (1, 3, 1, 2): 7,
    (1, 2, 1, 3): 8,
    (3, 1, 1, 2): 9,
}


def passcode_solve(data):
    # 행은 위에서 아래로
    # 열은 뒤에서 부터 읽으면서 코드 찾기

    for i in range(N):
        for j in range(M - 1, 54, -1):  # 55번까지 확인하고 없으면 없는거
            if data[i][j] == 1:  # 암호코드의 마지막 찾음
                # 지금부터 암호코드를 숫자(8개)로 변환
                code = []
                for _ in range(8):
                    # 숫자 1개 읽어오기
                    w1 = w2 = w3 = w4 = 0
                    # 1의 개수 세기
                    while data[i][j] == 1:
                        w4 += 1
                        j -= 1
                    # 0의 개수 세기
                    while data[i][j] == 0:
                        w3 += 1
                        j -= 1
                    # 1의 개수 세기
                    while data[i][j] == 1:
                        w2 += 1
                        j -= 1
                    # 0의 개수 구하기
                    w1 = 7 - w2 - w3 - w4
                    j -= w1

                    code.insert(0, code_dic[(w1, w2, w3, w4)])

                # 암호코드(code)가 정상인지 아닌지 판별
                odd_sum = code[0] + code[2] + code[4] + code[6]
                even_sum = code[1] + code[3] + code[5] + code[7]
                if (odd_sum * 3 + even_sum) % 10 == 0:
                    return odd_sum + even_sum
                else:
                    return 0

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = [list(map(int, input())) for _ in range(N)]

    # 뒤에서 부터 읽으면서 암호 코드 찾기
    print(f'#{tc}', passcode_solve(data))

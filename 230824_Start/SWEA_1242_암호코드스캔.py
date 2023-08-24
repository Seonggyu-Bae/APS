"""
암호 코드의 규칙
1. 총 8개의 숫자로 이루어져 있다
2. 앞 7자리는 상품 고유의 번호를 나타내며, 마지막 자리는 검증코드
 상품고유번호의 홀수 자리의 합 * 3 + 짝수 자리의 합 + 검증코드가 10의 배수이면 올바른 코드

암호코드는 16진수로 이루어져있음
이를 2진수로 변환하여 암호코드 정보확인

"""
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
hex_decimal = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
    '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}


def hex_to_bin(hex_num):
    ans = ''
    for h in hex_num:
        temp = []
        a = hex_decimal[h]
        for j in range(4):
            temp.insert(0, a % 2)
            a //= 2
        for i in range(4):
            ans += str(temp[i])
    return ans


def passcode_solve(data):
    # 행은 위에서 아래로
    # 열은 뒤에서 부터 읽으면서 코드 찾기
    code = []
    for i in range(N):
        for j in range(M - 1, -1, -1):  #
            if data[i][j] != 0:  # 암호코드의 마지막 찾음
                hex_code = []
                while True:
                    j -= 1
                    if data[i][j] == 0:
                        break
                    else:
                        hex_code.insert(0, data[i][j])
                temp = ''
                for c in hex_code:
                    temp += c
                code.append(temp)

    return code
"""             
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
"""
"""
각 숫자는 0과 1의 넓이 비로 표현
암호코드의 가로 길이가 길어질 경우
숫자 하나가 차지하는 길이는 7의 배수가 된다
0001011 = 00000011001111 = 9
"""

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    passcode = [list(input().rstrip()) for _ in range(N)]

    print(passcode_solve(passcode))

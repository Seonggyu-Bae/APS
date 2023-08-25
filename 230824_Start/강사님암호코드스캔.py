import sys

sys.stdin = open('sample_input (1).txt', 'r')

htob = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}
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
    (3, 1, 1, 2): 9
}


def solve():
    # 뒤에서 부터 읽어보기
    result = 0
    for i in range(N):
        # 16진수를 2진수로 바꾸면서 길이가 4배가 됨
        j = M * 4 - 1
        while j > 54:
            # 암호코드 시작점 확인
            if binary_data[i][j] == '1' and binary_data[i - 1][j] == '0':  # 암호코드 시작
                # 숫자 8개 읽어오기
                code = []
                for _ in range(8):
                    w1 = w2 = w3 = w4 = 0
                    while binary_data[i][j] == '1':
                        w4 += 1
                        j -= 1
                    while binary_data[i][j] == '0':
                        w3 += 1
                        j -= 1
                    while binary_data[i][j] == '1':
                        w2 += 1
                        j -= 1
                    rate = min(w2, w3, w4)
                    w2 //= rate
                    w3 //= rate
                    w4 //= rate
                    w1 = 7 - (w2 + w3 + w4)
                    j -= w1 * rate
                    code.append(code_dic[(w1, w2, w3, w4)])

                # 숫자 8개 찾음
                odd_sum = code[1] + code[3] + code[5] + code[7]
                even_sum = code[0] + code[2] + code[4] + code[6]
                if (odd_sum * 3 + even_sum) % 10 == 0:
                    # 정상 코드니까
                    result += odd_sum + even_sum
            j -= 1

    return result


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    data = [input() for _ in range(N)]
    binary_data = ['' for _ in range(N)]

    for i in range(N):
        for j in range(M):
            binary_data[i] += htob[data[i][j]]

    result = solve()
    print(f'#{tc} {result}')

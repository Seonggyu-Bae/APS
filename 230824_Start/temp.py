import sys

sys.stdin = open('sample_input (1).txt','r')

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


def solve():
    pass


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    passcode = [list(input().rstrip()) for _ in range(N)]
    codes = []

    for i in range(N):
        j = -1
        while j < M - 1:
            j += 1
            if passcode[i][j] != '0':
                code = ''
                while passcode[i][j] != '0':
                    code += passcode[i][j]
                    j += 1
                codes.append(code)

    delete_overlap = list(set(codes))
    print(delete_overlap)
    bin_codes = []
    for i in range(len(delete_overlap)):
        bin_codes.append(hex_to_bin(delete_overlap[i]))

    right = []

    for i in range(len(bin_codes)):
        multiple = len(bin_codes[i]) // 56

        if multiple < 1:
            continue
        print(bin_codes[i], multiple)
        for j in range(len(bin_codes[i]) - 1, -1, -1):
            if bin_codes[i][j] == '1':
                decimal_code = []
                for _ in range(8):
                    w1 = w2 = w3 = w4 = 0
                    while bin_codes[i][j] == '1':
                        w4 += 1
                        j -= 1
                    while bin_codes[i][j] == '0':
                        w3 += 1
                        j -= 1
                    while bin_codes[i][j] == '1':
                        w2 += 1
                        j -= 1
                    w1 = (7 * multiple) - w2 - w3 - w4
                    j -= w1
                    decimal_code.insert(0, code_dic[(w1 // multiple, w2 // multiple, w3 // multiple, w4 // multiple)])

                odd_sum = decimal_code[0] + decimal_code[2] + decimal_code[4] + decimal_code[6]
                even_sum = decimal_code[1] + decimal_code[3] + decimal_code[5] + decimal_code[7]
                if (odd_sum * 3 + even_sum) % 10 == 0:
                    right.append(odd_sum + even_sum)
                break
    if right:
        print(f'#{tc} {right[0]}')
    else:
        print(f'#{tc} 0')


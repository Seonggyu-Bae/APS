"""
16진수 >> 2진수 >> 10진수
16진수 문자로 이루어진 1차 배열이 주어질 때
앞에서부터 7bit씩 묶어 십진수로 변환하여 출력해보자
입력 예
0F97A3
000011111001011110100011
0000111 1100101 1110100 011
7       101     116     3
"""
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


def sevenbit_to_decimal(my_bin):
    bin_len = len(my_bin)
    ans = []
    for i in range(0, bin_len, 7):
        deci = 0
        n_l = bin_len - i
        if n_l < 7:
            for j in range(n_l):
                n_l -= 1
                deci += int(my_bin[i+j]) * 2**n_l
            ans.append(deci)
        else:
            temp = 6
            for j in range(7):
                deci += int(my_bin[i+j]) * 2**temp
                temp -= 1
            ans.append(deci)
    return ans


#hex_num = input()
print(hex_to_bin('C99624DDAF324C'))
#print(*sevenbit_to_decimal(hex_to_bin(hex_num)))

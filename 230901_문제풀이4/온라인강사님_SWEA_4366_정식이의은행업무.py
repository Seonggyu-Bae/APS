T = int(input())

for tc in range(1, T + 1):
    binary = input()
    ternary = list(map(int, input()))

    ans = 0

    bin_len = len(binary)  # 2진수가 몇자리인지
    ter_len = len(ternary)  # 3진수가 몇자리인지

    bin_to_decimal = int(binary, 2)  # 정수로 변환
    bin_list = [0] * bin_len  # 2진수의 각 비트를 반전시킨 수 bin_len개 저장

    for i in range(0, len(binary)):  # 각 비트를 반전시킨 2진수 만들기
        bin_list[i] = bin_to_decimal ^ (1 << i)  # ( ^ : XOR)

    for i in range(ter_len):  # 3진수의 B[i] 자리를 바꾼 숫자 만들기
        num1 = 0  # (ternary[i]+1) % 3
        num2 = 0  # (ternary[i]+2) % 3
        for j in range(ter_len):
            if i != j:
                num1 = num1 * 3 + ternary[j]
                num2 = num2 * 3 + ternary[j]
            else:
                num1 = num1 * 3 + (ternary[j] + 1) % 3
                num2 = num2 * 3 + (ternary[j] + 2) % 3

        if num1 in bin_list:
            ans = num1
            break   # for i
        if num2 in bin_list:
            ans = num2
            break

    print(ans)
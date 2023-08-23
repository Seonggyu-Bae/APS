"""
1. 입력사이에서 암호코드 찾아내기
2. 암호코드를 이루는 숫자 찾아내기
3. 암호코드가 정상인지 판단
4. 결과 출력
# 배경이 안거슬리시나요?
"""
passcode = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
            '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    code = [list(input()) for _ in range(N)]
    si, sj = 0, 0

    for i in range(N):
        for j in range(M - 1, -1, -1):
            if code[i][j] == '1':
                si, sj = i, j - 55
                break
    ans = []
    for k in range(sj, sj + 56, 7):
        temp = ''
        for l in range(7):
            temp += code[si][k + l]
        ans.append(passcode[temp])

    check = (ans[0] + ans[2] + ans[4] + ans[6]) * 3 + ans[1] + ans[3] + ans[5] + ans[7]

    if check % 10 == 0:
        passcode_sum = 0
        for num in ans:
            passcode_sum += num
        print(f'#{tc} {passcode_sum}')
    else:
        print(f'#{tc} 0')

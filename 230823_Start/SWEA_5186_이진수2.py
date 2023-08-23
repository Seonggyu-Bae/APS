T = int(input())

for tc in range(1, T+1):
    N = float(input())
    ans = ''
    count = 0
    one = 1
    temp = 0
    while count < 14:
        temp += one / 2
        if temp == N:
            ans += '1'
            break
        elif temp > N:
            temp -= one / 2
            ans += '0'
        else:
            ans += '1'
        count += 1
        one /= 2

    if count >= 13:
        print(f'#{tc} overflow')
    else:
        print(f'#{tc} {ans}')

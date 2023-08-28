import itertools

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    a, b, c, d = map(int, input().split())
    num = list(map(int, input().split()))

    ex = [None] * (a+b+c+d)

    for i in range(a):
        ex[i] = '+'
    for i in range(a, a+b):
        ex[i] = '-'
    for i in range(a+b, a+b+c):
        ex[i] = '*'
    for i in range(a+b+c, a+b+c+d):
        ex[i] = '/'

    b = []
    for p in itertools.permutations(ex, len(ex)):
        b.append(p)
    min_v = 100000000
    max_v = -100000000

    for i in range(len(b)):
        ans = num[0]
        k = 1
        for j in range(len(b[i])):
            if b[i][j] == '+':
                ans += num[k]
                k += 1
            elif b[i][j] == '-':
                ans -= num[k]
                k += 1
            elif b[i][j] == '*':
                ans *= num[k]
                k += 1
            else:
                if ans < 0 and num[k] > abs(ans):
                    ans = 0
                else:
                    ans //= num[k]
                k += 1
        if min_v > ans:
            min_v = ans
        if max_v < ans:
            max_v = ans

    print(f'#{tc} {max_v - min_v}')


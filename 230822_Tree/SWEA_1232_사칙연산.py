def postorder(p, N):
    global count1
    if p <= N:
        postorder(p * 2, N)
        postorder(p * 2 + 1, N)
        expression[count1] = temp[p]
        count1 += 1


def inorder(p, N):
    global count2

    if p <= N:
        inorder(p * 2, N)
        temp[count2] = N_info[p]
        count2 += 1
        inorder(p * 2 + 1, N)


def post_cal():
    S = []
    for c in expression:
        if c in '+-*/':
            if c == '+':
                a = S.pop()
                b = S.pop()
                S.append(a + b)
            elif c == '-':
                a = S.pop()
                b = S.pop()
                S.append(b - a)
            elif c == '*':
                a = S.pop()
                b = S.pop()
                S.append(a * b)
            else:
                a = S.pop()
                b = S.pop()
                S.append(b / a)

        else:
            S.append(int(c))

    return S[0]


for tc in range(1, 11):
    N = int(input())
    count1, count2 = 0, 0
    N_info = [0] * (N + 1)

    temp = [0] * N
    expression = [0] * N

    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)

    for i in range(N):
        info = input().split()
        info_len = len(info)
        if info_len == 4:
            N_info[i+1] = info[1]
            ch1[i+1] = info[2]
            ch2[i+1] = info[3]
        else:
            N_info[i+1] = info[1]

    inorder(1,N)
    postorder(1, N)
    print(expression)
    # print(f'#{tc} {int(post_cal())}')

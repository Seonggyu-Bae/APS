def lvr(root):
    if root:
        lvr(ch1[root])
        print(data[root], end='')
        lvr(ch2[root])


for tc in range(1, 11):
    N = int(input())

    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)
    data = [None] * (N + 1)

    for _ in range(N):

        info = input().split()
        temp = len(info)

        if temp == 4:
            pa = int(info[0])
            word = info[1]
            lc = int(info[2])
            rc = int(info[3])

            data[pa] = word
            ch1[pa] = lc
            ch2[pa] = rc

        elif temp == 3:
            pa = int(info[0])
            word = info[1]
            lc = int(info[2])

            data[pa] = word
            ch1[pa] = lc

        elif temp == 2:
            pa = int(info[0])
            word = info[1]

            data[pa] = word
    print(f'#{tc}',end=' ')
    lvr(1)
    print()

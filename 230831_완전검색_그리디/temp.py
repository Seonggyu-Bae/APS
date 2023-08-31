T = int(input())

for tc in range(1, T + 1):
    info, cnt = input().split()
    cnt = int(cnt)

    ES_set = set([info])
    temp = set()

    info_len = len(info)
    for _ in range(cnt):
        print('start', ES_set)
        while ES_set:
            num = ES_set.pop()
            num = list(num)

            for i in range(info_len):
                for j in range(i + 1, info_len):
                    num[i], num[j] = num[j], num[i]
                    temp.add(''.join(num))
                    print(temp)
                    num[i], num[j] = num[j], num[i]

        ES_set, temp = temp, ES_set
        print(ES_set)

    print(f'#{tc} {max(map(int, ES_set))}')

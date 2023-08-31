def change():
    global cnt
    if cnt == 0:
        return

    info_len = len(info)
    if info_len == 1:
        return
    if info_len == 2:
        if cnt % 2 == 0:
            return
        else:
            info[0], info[1] = info[1], info[0]
            return

    temp_idx = 0
    temp = '0'
    for i in range(1, info_len):
        if info[i] >= temp:
            temp_idx = i
            temp = info[i]

    for i in range(0, info_len):
        if temp > info[i]:
            info[i], info[temp_idx] = info[temp_idx], info[i]
            cnt -= 1
            break
    else:
        info[info_len-1], info[info_len-2] = info[info_len-2], info[info_len-1]
        cnt -= 1
    change()


T = int(input())

for tc in range(1, T + 1):
    info, cnt = input().split()
    info = list(info)
    cnt = int(cnt)
    change()
    print(f'#{tc}',info )

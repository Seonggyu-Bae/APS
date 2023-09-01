def solve(l, change_cnt, cnt, checked):
    global max_reward
    reward = int(''.join(info))

    if change_cnt == cnt:
        if reward > max_reward:
            max_reward = reward
        return

    if (cnt, reward) in checked:  # 수행 해 본 케이스
        return
    checked.add((cnt, reward))

    for i in range(l):
        for j in range(i + 1, l):
            info[i], info[j] = info[j], info[i]
            solve(l, change_cnt + 1, cnt, checked)
            info[i], info[j] = info[j], info[i]


T = int(input())

for tc in range(1, T + 1):
    info, cnt = input().split()
    cnt = int(cnt)
    max_reward = 0
    info = list(info)
    L = len(info)
    a = set()
    solve(L, 0, cnt, a)

    print(f'#{tc} {max_reward}')

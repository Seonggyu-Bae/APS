for tc in range(1, 11):
    N = int(input())
    is_possible = True

    for i in range(N):
        n_info = input().split()
        info_len = len(n_info)
        if not is_possible:
            continue
        if ((info_len == 3 or info_len == 4) and n_info[1] not in '+-*/') or (info_len == 2 and n_info[1] in '+-*/'):
            is_possible = False

    if is_possible:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')





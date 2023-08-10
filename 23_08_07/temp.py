def is_palindrome(my_arr):
    for i in range(N):
        for j in range(N - M + 1):
            if my_arr[i][j:j + M] == my_arr[i][j:j + M][::-1]:
                print(f'#{tc} {my_arr[i][j:j + M]}')
                return

    for k in range(N - M + 1):
        for l in range(N):
            col_list = []
            for m in range(M):
                col_list.append(my_arr[k + m][l])
            if col_list == col_list[::-1]:
                print(f'#{tc}', ''.join(col_list))
                return
    return False

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    word_line = [input() for _ in range(N)]

    is_palindrome(word_line)

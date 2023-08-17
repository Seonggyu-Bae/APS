for tc in range(1, 11):
    # 8 X 8 평면 글자판에서 입력받은 길이를 가진 회문의 갯수를 구하는 문제임
    palindrome_len = int(input())
    word_board = list(input() for _ in range(8))
    check_len = palindrome_len // 2

    count = 0  # 회문의 개수를 저장할 변수

    for i in range(8):
        for j in range(9 - palindrome_len):
            row_len_check = 0
            col_len_check = 0
            # 행 탐색
            for k in range(check_len + 1):
                if word_board[i][j + k] == word_board[i][j + palindrome_len - k - 1]:
                    row_len_check += 1
                    if row_len_check == check_len:
                        count += 1
                        break
                else:
                    break
            # 열 탐색
            for l in range(check_len + 1):
                if word_board[j + l][i] == word_board[j + palindrome_len - l - 1][i]:
                    col_len_check += 1
                    if col_len_check == check_len:
                        count += 1
                        break
                else:
                    break

    print(f'#{tc} {count}')

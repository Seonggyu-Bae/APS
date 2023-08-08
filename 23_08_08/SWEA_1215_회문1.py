for tc in range(1,11):
    palindrome_len = int(input())
    word_board = list(input() for _ in range(8))

    count = 0

    for i in range(8):
        for j in range(9-palindrome_len):
            temp = 0
            for k in range(j,j+palindrome_len//2+1):
                print(i,k,word_board[i][k], i,palindrome_len-k-1,word_board[i][palindrome_len-k-1] )
                if word_board[i][k] == word_board[i][palindrome_len-k-1]:
                    temp += 1
                    if temp == palindrome_len//2:
                        print(k, palindrome_len-k-1 )
                        count += 1
                        break
                else:
                    break

    """for i in range(9-palindrome_len):
        temp = 0
        for j in range(i, i+palindrome_len//2+1):
            if word_board[j][i] == word_board[i+palindrome_len-1-j][i]:
                temp += 1
                if temp == palindrome_len//2:
                    count += 1
            else:
                temp = 0"""

    print(f'#{tc} {count}')

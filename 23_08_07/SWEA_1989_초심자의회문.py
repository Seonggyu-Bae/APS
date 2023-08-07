T = int(input())

for tc in range(1, T + 1):
    word = str(input())
    is_true = 1
    for i in range(len(word)):
        if word[i] != word[len(word)-1-i]:
            is_true = 0

    print(f'#{tc} {is_true}')



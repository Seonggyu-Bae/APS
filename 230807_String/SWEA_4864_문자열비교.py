T = int(input())

for tc in range(1, T+1):
    str1 = str(input())
    str2 = str(input())
    is_true = 0
    count = 0

    for i in range(len(str2)-len(str1)+1):
        for j in range(len(str1)):
            if str1[j] == str2[i+j]:
                count += 1
                if count == len(str1):
                    is_true = 1
                    break
            else:
                count = 0
                break

    print(f'#{tc} {is_true}')

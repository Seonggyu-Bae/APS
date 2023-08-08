T = int(input())

for tc in range(1, T+1):
    s1 = str(input())
    s2 = str(input())
    s1_len = len(s1)
    s2_len = len(s2)
    max_count = 0

    for i in range(s1_len):
        temp = 0
        for j in range(s2_len):
            if s1[i] == s2[j]:
                temp += 1
        if temp > max_count:
            max_count = temp

    print(f'#{tc} {max_count}')


for _ in range(10):
    tc = int(input())
    str1 = str(input())
    str2 = str(input())

    str1_len = len(str1)
    str2_len = len(str2)

    count = 0                               # 몇번 나오는지 저장할 변수

    for i in range(str2_len-str1_len+1):    # 특정한 문자열의 길이를 감안해서 탐색 범위 설정
        len_count = 0
        for j in range(str1_len):           # 특정한 문자열이 있는지 찾아야함
            if str1[j] == str2[i+j]:        # 한 글자가 같으면
                len_count += 1              # 길이를 하나올리고
                if len_count == str1_len:   # 길이가 특정한 문자열의 길이와 같다면
                    count += 1              # 특정한 문자열이니까 카운트 올림

    print(f'#{tc} {count}')


"""
14번라인 if str1[j] == str2[i+j]:
str1 = 'ab' str2 = 'acbde' 라면
i=0, j=0가 0일때는 
a a비교
i=0 j=1일때는
b와 c 비교  
"""
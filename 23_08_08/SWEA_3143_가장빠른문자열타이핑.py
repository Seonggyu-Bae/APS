T = int(input())

for tc in range(1,T+1):
    A,B = input().split()

    A_len = len(A)
    B_len = len(B)
    min_type_count = 0
    i = -1

    # 조건에따라 i를 증가시키면서 반복을 돌려야해서 while문을 사용하였음
    # C언어와 다르게 파이썬에서는 for문에서 i 를 증가시켜도 그 순간에만 먹히고 그 이후에는 원래대로 돌아감
    while i < A_len-1:
        i += 1
        count = 0   #

        # A의 남은 검사할 길이가 B의 길이보다 짧다면
        # A의 남은 길이만큼 타이핑 횟수를 늘리고 break
        if A_len - i < B_len:
            min_type_count += A_len - i
            break

        for j in range(B_len):
            if B[j] == A[i+j]:          # 같으면
                count += 1              # count 증가시키고
                if count == B_len:      # count가 B의 길이와 같다면
                    min_type_count += 1 # 타이핑 횟수 증가시키고
                    i += B_len-1        # A 탐색 인덱스(i)를 B_len-1 만큼 증가시킴
                                        # i는 while 시작하면 1증가하기 때문에 -1 해준거임

            else:                       #다르면
                count = 0               #count 초기화하고
                min_type_count += 1     #타이핑횟수올리고 다음꺼 보러감
                break

    print(f'#{tc} {min_type_count}')




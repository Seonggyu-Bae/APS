def find_palindrome():
    for i in range(N):
        for j in range(N - M + 1):  # j 회문검사 시작점
            # 회문검사 시작
            # (최대)회문의 길이 절반만큼 검사
            for k in range(M // 2):
                if data[i][j + k] != data[i][j + M - 1 - k]:
                    break
            else:  # for 문에서 break가 한번도 수행되지 않으면 실행
                # 회문찾음
                result = []
                for k in range(j, j + M):
                    result.append(data[i][k])
                return ''.join(result)

    for i in range(N):
        for j in range(N - M + 1):  # j 회문검사 시작점
            # 회문검사 시작
            # (최대)회문의 길이 절반만큼 검사
            for k in range(M // 2):
                if data[j + k][i] != data[j + M - 1 - k][i]:
                    break
            else:  # for 문에서 break가 한번도 수행되지 않으면 실행
                # 회문찾음
                result = []
                for k in range(j, j + M):
                    result.append(data[k][i])
                return ''.join(result)

    return []  # 얘는 실행안될건데...넣어주면 이쁘니까


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]
    # N * N 행렬에서
    # 일단...각 행에 회문이 있는지 검사
    result = find_palindrome()
    print(f'#{tc} {result}')
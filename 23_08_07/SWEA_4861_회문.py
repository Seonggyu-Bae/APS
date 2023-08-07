T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())

    word_line = [input() for _ in range(N)]
    count = 0
    ans = []
    ans1 = ''
    for i in range(N):
            for k in range(N-M+1):
                for l in range(M//2):
                    if word_line[i][k+l] != word_line[i][N-k-l-1]:
                        count = 0
                        ans = []
                        continue
                    else:
                        count += 1
                        ans.append(word_line[i][k+l])
                        if count == M//2:
                            ans1 + str(ans)
                            ans.append(ans[-1::-1])
                            print(ans1)
                            break

    for i in range(N):
        for k in range(N - M + 1):
            for l in range(M//2):
                if word_line[k + l][i] != word_line[N - k - l-1][i]:
                    ans = []
                    count = 0
                    continue
                else:
                    count += 1
                    ans.append(word_line[i][k + l])
                    if count == M//2:
                        ans.append(ans[-1::])
                        print(ans)
                        break

    ans.append(ans[-1::])
    print(''.join(str(ans)))
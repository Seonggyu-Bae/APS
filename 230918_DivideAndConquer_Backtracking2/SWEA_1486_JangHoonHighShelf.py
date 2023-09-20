from itertools import combinations

T = int(input())

for tc in range(1, T + 1):
    # N명의 점원, 선반의 높이 B
    N, B = map(int, input().split())

    # 점원의 키 H
    H = list(map(int, input().split()))

    m_h = 200000
    ans = 200000

    for i in range(N):
        # N명중에 i(1~10)명 뽑는 조합을 만들어서 돌림
        a = list(combinations(range(N), i + 1))
        for j in range(len(a)):
            temp = 0
            for l in range(len(a[j])):
                if temp >= m_h:
                    break
                temp += H[a[j][l]]

            if temp >= B:
                if temp - B < ans:
                    ans = temp - B
                    m_h = temp

    print(f'#{tc} {ans}')

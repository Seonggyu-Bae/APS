"""
불일치가 발생한 텍스트 스트링의 앞 부분에 어떤 문자가 있는지를
미리 알고 있으므로, 불일치가 발생한 앞 부분에 대하여 다시 비교하지 않고 매칭 수행

패턴을 전처리하여 배열 next[M]을 구해서 잘못된 시작을 최소화
next[M] : 불일치가 발생했을 경우 이동할 다음 위치

시간 복잡도 : O(M+N)
"""


def kmp(t,p):
    N = len(t)
    M = len(p)

    lps = [0] * (M+1)

    #preProcessing
    j = 0       # 일치한 개수 == 비교할 패턴 위치
    lps[0] = -1

    for i in range(1,M):
        lps[i] = j              #p[i] 이전에 일치한 개수
        if p[i] == p[j]:
            j+=1
        else:
            j=0
    lps[M] = j
    print(lps)


    #아래 부터 Search 과정
    i = 0       # 비교할 텍스트 위치
    j = 0       # 비교할 패턴 위치


    while i < N and j <= M:
        if j == -1 or t[i] == p[j]:     # 첫 글자가 불일치 했거나, 일치하면
            i += 1
            j += 1
        else:                           # 불일치
            j = lps[j]
        if j == M:                      # 패턴을 찾을 경우
            print(i-M, end = ' ')       # 패턴의 인덱스 출력
            j = lps[j]
    print()
    return

t = 'abcdefghabcdabcefefkajfabcdabcef'
p = 'abcdabcef'

kmp(t,p)

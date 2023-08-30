# 부분집합, 조합은 DFS임?
# 조합 : 전체에서 주어진 개수만큼 선택
# 각 요소가 조합에 포함되는지 아닌지 결정하는 것은 부분집합정할때랑 동일함
# 포함되는 요소의 개수가 정해져 있는것이 다르다.
def comb(idx, cnt):  # cnt : 이때가지 몇개의 요소가 선택되었는지 알려주는 변수
    if cnt == M: # 필요한 만큼 골랐음
        print(selected)
        return

    if idx == N:  # 모든 요소에 대해 조합 여부 결정했지만 필요한만큼 고르진 않음
        return    # 이 코드로 치면 3개 중에 2개를 못고른거임

    selected[idx] = 1
    comb(idx + 1, cnt + 1)
    selected[idx] = 0
    comb(idx + 1, cnt)
    pass


a = ['A', 'B', 'C']
N = len(a)
M = 2   # 선택할 요소의 개수
# 각 요소 포함여부 표시배열
selected = [0] * N

# comb(idx,cnt)
# 요소의 idx
# 선택된 요소의 개수 == cnt
comb(0, 0)

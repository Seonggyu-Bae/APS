# 순열
# p의 idx 번째 요소에 들어갈 수 있는거 다 넣어보기
def permutation(idx):
    if idx == N:
        print(p)
        return

    for i in range(N):
        # 요소의 중복 사용을 방지
        if not used[i]:
            p[idx] = a[i]
            used[i] = 1
            permutation(idx + 1)
            used[i] = 0

a = [1, 2, 3]
N = len(a)
used = [0] * N  # 각 요소가 사용되었는지 표시하는배열
p = [None] * N

permutation(0)

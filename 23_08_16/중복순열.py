# perm_arr[idx]에 들어갈 수 있는 것 다 넣어보기
def perm(idx):
    if idx == N:
        print(perm_arr)
        return

    for i in range(N):
        perm_arr[idx] = arr[i]
        perm(idx+1)

arr = [1, 2, 3]
N = 3

perm_arr = [0] * N

perm(0)
# perm_arr[idx]에 들어갈 수 있는 것 다 넣어보기
def perm(idx,used):
    if idx == N:
        print(perm_arr)
        return

    for i in range(N):
        # 앞에서 넣은건 넣지말자
        if used[i] == 0:        # 백트래킹 기법(잘라내기)
            perm_arr[idx] = arr[i]
            used[i] = 1 # i번째 요소를 사용했음을 표시
            perm(idx+1, used)
            used[i] = 0 # i번째 요소에 대해 사용이 끝남

arr = [1, 2, 3]
N = 3

perm_arr = [0] * N
used = [0] * N
perm(0,used)


def perm2(idx):
    if idx == N:
        print(arr)
        return
    # 할 수 있는 일 다 해보기
    # 안바꾸거나 뒤에 있는 요소와 자리 바꾸거나
    for i in range(idx, N):
        arr[idx], arr[i] = arr[i], arr[idx]
        perm2(idx+1)
        arr[idx], arr[i] = arr[i], arr[idx]

print()
perm2(0)
arr = [i for i in range(1,11)]
N = 10
selected = [0] *  N
# 부분집합의 합, 필요 없는 경우의 수를 더 이상 수행하지 않기 위해
# 중간합이 필요함
def solve(idx, sum_v):
    if sum_v > 10:      #만약 부분집합의 합이 10인 것을 찾고있다면 중간에 합이 10이넘어가면 더 볼필요가없음
        return
    elif sum_v == 10:
        for i in range(N):
            if selected[i]:
                print(arr[i], end=' ')
        print()
        return
    if idx == N:        # 마지막 인덱스 까지 봤는데 10보다 작으면?
        return

    # idx 번째 요소를 부분집합에 포함하느냐 마느냐?
    selected[idx] = 1
    solve(idx+1, sum_v + arr[idx])
    selected[idx] = 0
    solve(idx+1, sum_v)


solve(0,0)
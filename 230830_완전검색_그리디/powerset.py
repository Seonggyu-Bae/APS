#  부분집합
# idx 번째 요소가 부분집합에 포함되는지 결정
def power_set(idx):
    if idx == N:        # 모든 요소에 대해 부분집합을 포함 여부가 결정됨
        # 그룹핑 가능
        g1 = []
        g2 = []
        print(selected)
        for i in range(N):
            if selected[i]:
                g1.append(a[i])
            else:
                g2.append(a[i])
        # 그룹된거 이어져있는지는 DFS,BFS, 서로소집합을 사용해서 확인가능
        print(g1, g2)
        return

    #for i in range(2):
        #selected[idx] = i
        #power_set(idx+1)

    # idx번째 요소를 부분집합에 포함시키거나
    selected[idx] = 1
    power_set(idx + 1)
    # idx번째 요소를 부분집합에 포함시키지 않거나
    selected[idx] = 0
    power_set(idx+1)



a = [1, 2, 3]
N = len(a)

selected = [0] * N  # 각 요소의 부분집합 여부를 표시할 배열

power_set(0)
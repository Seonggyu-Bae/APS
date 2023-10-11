from itertools import combinations
from collections import deque

def solve(sec):
    start = sec[0]
    q = deque([start])
    visited = set([start])
    pop_sum = 0

    while q:
        v = q.popleft()
        pop_sum += population[v-1]
        for i in range(1,N+1):
            if info[v][i] == 1 and i not in visited and i in sec:
                q.append(i)
                visited.add(i)

    return pop_sum, len(visited)


N = int(input())
population = list(map(int,input().split()))

info = [[0] * (N+1) for _ in range(N+1)]

for idx in range(N):
    data = list(map(int, input().split()))
    for i in range(1,data[0]+1):
        info[idx+1][data[i]] = 1
        info[data[i]][idx+1] = 1

ans = 10000

for i in range(1, N//2+1):
    divide = list(combinations(range(1,N+1),i))
    for sector in divide:
        sum1, v1 = solve(sector)
        sum2, v2 = solve([i for i in range(1,N+1) if i not in sector])
        if v1 + v2 == N:
            ans = min(ans,abs(sum1-sum2))

if ans == 10000:
    print(-1)
else:
    print(ans)

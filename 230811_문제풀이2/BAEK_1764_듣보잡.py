N, M = map(int, input().split())

nohear = [input() for _ in range(N)]
nosee = [input() for _ in range(M)]

nohearandsee = []

for i in range(N):
    for j in range(M):
        if nohear[i] == nosee[j]:
            nohearandsee.append([nohear[i]])

sort(nohearandsee)
print(nohearandsee)
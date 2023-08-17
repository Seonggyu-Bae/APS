N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

total1 = 0
total2 = 0

for i in range(N):
    total1 += arr[i][i]
    print(total1,i,i)
    total2 += arr[i][N-1-i]
    print(total2,i,N-1-i)
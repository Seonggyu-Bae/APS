N = int(input())

my_arr = [list(map(int,input().split())) for _ in range(N)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
my_sum = 0

for i in range(N):
    for j in range(N):
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < 5 and 0 <= nj < 5:  # is index valid?
                my_del = my_arr[i][j] - my_arr[ni][nj]
                if my_del > 0:
                    my_sum += my_del
                else:
                    my_sum += -my_del

print(my_sum)

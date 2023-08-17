N = int(input())
my_list = [0, ] * (N + 1)
for i in range(1, N + 1):
    temp = i
    while temp:
        if temp % 10 == 3 or temp % 10 == 6 or temp % 10 == 9:
            my_list[i] += 1
        temp //= 10

for i in range(1, N + 1):
    if my_list[i] == 0:
        print(f'{i}', end=' ')
    else:
        for j in range(my_list[i]):
            print('-', end='')
        print('', end=' ')

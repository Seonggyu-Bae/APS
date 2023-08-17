T = int(input())

for tc in range(1,T+1):
    N = int(input())

    num_list = list(map(int, input()))

    temp = 0
    count = 0
    for i in range(len(num_list)):
        if num_list[i] == 1:
            temp += 1
            if temp > count:
                count = temp
        else:
            temp = 0

    print(f'#{tc} {count}')
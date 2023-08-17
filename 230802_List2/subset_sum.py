my_lst = [0]*10
for i in range(10):
    my_lst[i] = int(input())

is_possible = False

for i in range(10):
    if my_lst[i] == 0:
        is_possible = True
        break

    sub_lst = [0] * 10
    subset_sum = 0
    subset_sum += my_lst[i]
    for j in range(10):
        if j != i:
            subset_sum += my_lst[j]
            print('j', j, 'sub', subset_sum)
        if subset_sum == 0:
            is_possible = True
            break

    if is_possible:
        break

print(is_possible)

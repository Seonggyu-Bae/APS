def counting_sort(my_lst, max_num):
    # 카운트 배열
    count_list = [0] * (max_num + 1)  # ( o to max_num)

    # 정렬된 배열
    c_sort_list = [0] * len(my_lst)

    for i in range(len(my_lst)):
        count_list[my_lst[i]] += 1

    for i in range(1, len(count_list)):
        count_list[i] += count_list[i - 1]

    for i in range(len(my_lst) - 1, -1, -1):
        count_list[my_lst[i]] -= 1
        c_sort_list[count_list[my_lst[i]]] = my_lst[i]

    return c_sort_list


T = int(input())

for _ in range(T):
    tc, s_len = input().split()
    my_str = list(input().split())

    num = ("ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN")

    new_str = []
    for i in range(int(s_len)):
        new_str.append(num.index(my_str[i]))

    new_str = counting_sort(new_str, 9)

    for i in range(int(s_len)):
        new_str[i] = num[new_str[i]]

    print(tc)
    print(*new_str)

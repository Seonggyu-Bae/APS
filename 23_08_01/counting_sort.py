"""
def counting_sort(my_lst, max_num):
    count_list = [0] * (max_num + 1)  # ( o to max_num)

    countsort_lst = []

    for i in range(len(my_lst)):
        count_list[my_lst[i]] += 1

    for i in range(0, max_num + 1):
        for j in range(count_list[i]):
            countsort_lst.append(i)

    print(countsort_lst)


a = [1, 32, 4, 5, 65, 25, 6, 3, 4, 32, 342, 4, 45, 0, 0, 0, 0, 7, 65, 4, 64, 3, 253, 23, 1, 2, 3, 4, 5, 6, 7]
counting_sort(a, 342)"""


# 진정한 counting sort
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

    print(c_sort_list)


a = [1, 32, 4, 5, 65, 25, 6, 3, 4, 32, 342, 4, 45, 0, 0, 0, 0, 7, 65, 4, 64, 3, 253, 23, 1, 2, 3, 4, 5, 6, 7]
counting_sort(a, 342)

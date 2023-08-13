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
# 평균 수행시간 O(N+K)
# N이 비교적 작을 때만 가능
def counting_sort(Data, max_num):
    # 카운트 배열
    count_list = [0] * (max_num + 1)  # ( o to max_num)

    # 정렬된 배열
    c_sort_list = [0] * len(Data)


    # 1단계
    # Data에서 각 항목들의 발생 회수를 세고, 정수 항목들로 직접 인덱스되는 count_list에 저장
    for i in range(len(Data)):
        count_list[Data[i]] += 1

    # 2단계
    # 정렬된 집합에서 각 항목의 앞에 위치할 항목의 개수를 반영하기 위해 count_list 원소를 조정
    for i in range(1, len(count_list)):
        count_list[i] += count_list[i - 1]

    # 정렬시작
    for i in range(len(Data) - 1, -1, -1):
        count_list[Data[i]] -= 1
        c_sort_list[count_list[Data[i]]] = Data[i]
    return c_sort_list


Data = [1, 32, 4, 5, 65, 25, 6, 3, 4, 32, 342, 4, 45, 0, 0, 0, 0, 7, 65, 4, 64, 3, 253, 23, 1, 2, 3, 4, 5, 6, 7]
counting_sort(Data, 342)

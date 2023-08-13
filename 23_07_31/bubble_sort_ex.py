"""
Bubble sort
인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 방식
1. 첫 번째 원소부터 인접한 원소끼리 계속 자리를 교환하면서 맨 마지막 자리까지 이동한다.
2. 한 단계가 끝나면 가장 큰 원소가 마지막 자리로 정렬된다.
시간 복잡도 O(N^2)
"""


def bubble_sort(my_list):
    my_len = len(my_list)
    for i in range(my_len - 1, 0, -1):      # 한 단계가 끝나면 가장 큰 원소가 마지막 자리로 가게 만들기 위해
        for j in range(0, i):               # i가 마지막 인덱스 부터 1 씩 줄어드니까 요래 만들면 가능
            if my_list[j] > my_list[j + 1]:
                print(my_list)
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
                print(my_list)
    return my_list


m_list = [241, 12, 1535, 4, 421, 42432, 322, 32, 1, 4124, 51, 4, 14]

print(bubble_sort(m_list))

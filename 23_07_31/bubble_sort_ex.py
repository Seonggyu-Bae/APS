def bubble_sort(my_list):
    my_len = len(my_list)
    for i in range(my_len-1,0,-1):
        for j in range(0,i):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    return my_list


m_list = [241, 12, 1535, 4, 421, 42432, 322, 32, 1, 4124, 51, 4, 14]

print(bubble_sort(m_list))
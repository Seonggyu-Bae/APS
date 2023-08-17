def special_sort(arr_len, my_arr):
    for i in range(arr_len):
        if i % 2 == 0:
            max_idx = i
            for j in range(i + 1, arr_len):
                if my_arr[max_idx] < my_arr[j]:
                    max_idx = j
            my_arr[i], my_arr[max_idx] = my_arr[max_idx], my_arr[i]
        else:
            min_idx = i
            for j in range(i + 1, arr_len):
                if my_arr[min_idx] > my_arr[j]:
                    min_idx = j
            my_arr[i], my_arr[min_idx] = my_arr[min_idx], my_arr[i]
    return my_arr


# 입력으로 1, 10, 1 2 3 4 5 6 7 8 9 10을 주었을 때, 출력 결과를 확인합니다.
data_len = 10
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = special_sort(data_len, data)
print(result)  # [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]

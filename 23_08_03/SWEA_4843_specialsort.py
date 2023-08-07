def special_sort(ans, arr_len):
    for i in range(arr_len):
        if i % 2 == 0:
            max_i = i
            for j in range(i + 1, arr_len):
                if ans[max_i] < ans[j]:
                    max_i = j
            ans[i], ans[max_i] = ans[max_i], ans[i]
        else:
            min_i = i
            for j in range(i + 1, arr_len):
                if ans[min_i] > ans[j]:
                    min_i = j
            ans[i], ans[min_i] = ans[min_i], ans[i]

    return ans


T = int(input())

for tc in range(1, T + 1):
    data_len = int(input())
    data = list(map(int, input().split()))
    # 결과를 10개까지만 출력
    answer = ' '.join(map(str,(special_sort(data, data_len)[:10])))
    print(f'#{tc} {answer}')


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
n = len(arr)
count = 0
for i in range(1 << n):  # 1<<n : 부분 집합의 개수
    sum_temp = 0
    sum_count = 0
    for j in range(n):  # 원소의 수만큼 비트를 비교함
        if i & (1 << j):  # i의 j번 비트가 1인경우
            print(arr[j], end=", ")  # j번 원소 출력
    print()

"""def print_subset(bit, arr, n):
    total = 0
    for i in range(n):
        if bit[i]:
            print(arr[i], end=' ')
            total += arr[i]
    print(bit, total)


arr = [1, 2, 3, 4]
bit = [0, 0, 0, 0]
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                print_subset(bit,arr,4)"""

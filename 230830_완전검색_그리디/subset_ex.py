arr = [1, 2, 3, 4]
n = len(arr)

for i in range(0, (1 << n)):  # 1<<n : 부분집합의 개수 (1을 왼쪽으로 n만큼밀면 2^n)
    subset1 = []
    subset2 = []
    for j in range(0, n):
        if i & (1 << j):  # i번째 비트가 1이면
            subset1.append(arr[j])
        else:
            subset2.append(arr[j])
    print(subset1, subset2)
print()
# 공집합을 제외하고 반반 나눔
for i in range(1, (1 << n) - 1):  # 1<<n : 부분집합의 개수 (1을 왼쪽으로 n만큼밀면 2^n)
    subset1 = []
    subset2 = []
    for j in range(0, n):
        if i & (1 << j):  # i번째 비트가 1이면
            subset1.append(arr[j])
        else:
            subset2.append(arr[j])
    print(subset1, subset2)
print()

# 공집합을 제외하고 반반 나누는데 중복을 제거
# for i in range(1, (1 << n) - 1):    # 1<<n : 부분집합의 개수 (1을 왼쪽으로 n만큼밀면 2^n)
for i in range(1, (1 << n) // 2):   # (1<<n)//2 == 1 <<(n-1)
    subset1 = []
    subset2 = []
    total1 = 0
    total2 = 0
    for j in range(0, n):
        if i & (1 << j):  # i번째 비트가 1이면
            subset1.append(arr[j])
            total1 += arr[j]
        else:
            subset2.append(arr[j])
            total2 += arr[j]
    r1 = f(subset1)
    r2 = f(subset2)
    if r1 and r2:
        if min_v > abs(total1 - total2):
            print()
    print(subset1, subset2)

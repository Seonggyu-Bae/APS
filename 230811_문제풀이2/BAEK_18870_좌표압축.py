import sys


def binary_search(my_lst, value):
    start = 0
    end = len(my_lst)-1
    while start <= end:
        mid = (start + end) // 2
        if my_lst[mid] == value:
            return mid
        elif my_lst[mid] > value:
            end = mid - 1
        else:
            start = mid + 1
    return 0


N = int(input())
X = list(map(int, sys.stdin.readline().split()))

X1 = sorted(set(X))
for i in range(N):
    print(binary_search(X1, X[i]),end=' ')

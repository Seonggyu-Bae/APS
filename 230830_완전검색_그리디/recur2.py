# 배열 arr에 key 가 있으면 1 없으면 0을 리턴하는 함수
def f(i, N, key, arr):  # i : 현재상태, N : 목표, key : 찾고자 하는 값
    if i == N:
        return 0
    elif arr[i] == key:
        return 1
    else:
        return f(i + 1, N, key, arr)


N = 5
A = [1, 2, 3, 4, 5]
B = [0] * N
key = 3
print(f(0, N, key, A))

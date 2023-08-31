# 부분집합 합 문제 구현하기
# arr 에 있는 정수 집합에 대한 모든 부분집합중 원소의 합이 0이 되는 부분집합을 모두 출력하시오
def subset(i, N):
    if i == N:
        s = 0
        for j in range(N):
            if bit[j]:
                s += arr[j]
        if s == 0:
            for j in range(N):
                if bit[j]:
                    print(arr[j], end=' ')
            print()
    else:
        bit[i] = 1
        subset(i + 1, N)
        bit[i] = 0
        subset(i + 1, N)


arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
N = len(arr)
bit = [0] * N

subset(0, N)

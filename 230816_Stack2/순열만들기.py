"""
A[1, 2, 3]의 모든 원소를 사용한 순열
123, 132, 213, 231, 312, 321
총 6가지 경우
"""


# visited[] 를 사용하지 않는 방법

def f(i, N):
    global cnt
    cnt += 1
    if i == N:
        print(A)
    else:
        for j in range(i, N):  # 자신부터 오른쪽 끝까지
            A[i], A[j] = A[j], A[i]
            f(i + 1, N)
            A[i], A[j] = A[j], A[i] # 원상복구
cnt = 0
N = 5
A = [i for i in range(N)]
f(0, N)
print(cnt)

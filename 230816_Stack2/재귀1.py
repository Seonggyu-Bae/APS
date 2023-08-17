def f(i, N):
    if i == N:
        return
    else:
        B[i] = A[i]
        f(i + 1, N)

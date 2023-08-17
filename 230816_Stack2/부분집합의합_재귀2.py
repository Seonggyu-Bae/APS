def f(i, N, sub_sum): # sub_sub : i-1 원소까지 부분집합의 합(포함된 원소의 합)
    if i == N:
        print(bit, end= ' ')
        print(f' : {sub_sum}')
        return
    else:
        bit[i] = 1              # 부분집합에 A[i] 포함
        f(i + 1, N,sub_sum+A[i])
        bit[i] = 0              # 부분집합에 A[i] 빠짐
        f(i + 1, N, sub_sum)
        return


A = [1, 2, 3]
bit = [0] * 3
f(0, 3, 0)

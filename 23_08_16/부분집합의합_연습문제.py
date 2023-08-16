def f(i, N, sub_sum, target):  # sub_sub : i-1 원소까지 부분집합의 합(포함된 원소의 합)
    global cnt                 # target : 찾으려는 합
    cnt += 1
    if sub_sum == target:
        print(bit)
        return
    elif i == N:
        return  # 남은 원소가 없는경우
    elif sub_sum > target:
        return
    if i == N:
        if sub_sum == 10:
            print(bit)
        return
    else:
        bit[i] = 1  # 부분집합에 A[i] 포함
        f(i + 1, N, sub_sum + A[i],target)
        bit[i] = 0  # 부분집합에 A[i] 빠짐
        f(i + 1, N, sub_sum, target)
        return


# 1부터 10까지 원소인 집합, 부분집합의 합이 10인경우
N = 10
A = [i for i in range(1, N + 1)]
bit = [0] * N
cnt = 0
f(0, N, 0, 10)
print(cnt)


"""
평균적으로 백트래킹기법을 사용하면 DFS 보다 빠르지만
최악의경우 DFS와 같음
"""
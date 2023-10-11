def solve(idx, cnt):
    global is_possible

    if idx == N:
        if cnt != 0:
            print(idx,cnt)
            is_possible = False
            return
        else:
            return

    if cnt == 2:
        if h[idx] - tree[idx] >= 2:
            tree[idx] += 2
        elif h[idx] - tree[idx] == 1:
            tree[idx] += 1
            solve(idx + 1, 1)
        else:
            solve(idx + 1, 2)

    if cnt == 1:
        if h[idx] - tree[idx] >= 1:
            tree[idx] += 1
        else:
            solve(idx + 1, 1)

    while tree[idx] != h[idx]:
        if h[idx] - tree[idx] > 3:
            tree[idx] += 3
        elif h[idx] - tree[idx] == 2:
            tree[idx] += 2
            solve(idx + 1, 1)
        else:
            tree[idx] += 1
            solve(idx + 1, 2)


def ans():
    for i in range(N):
        if tree[i] != h[i]:
            return False
    return True


is_possible = True
N = int(input())
tree = [0] * N
h = list(map(int, input().split()))

solve(0, 0)
print(tree)
if is_possible:
    print('YES')
else:
    print('NO')

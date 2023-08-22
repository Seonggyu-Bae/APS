def inorder(p, N):  # N은 완전 이진트리의 마지막 정점

    if p <= N:
        inorder(p * 2, N)
        print(tree[p], end='')
        inorder(p * 2 + 1, N)


T = 10

for tc in range(1, T + 1):
    N = int(input())

    # 어떻게 저장해야 문제를 풀 때 편할까를 생각해야한다.

    tree = [0] * (N + 1)  # N번 노드까지 있는 완전이진트리
    for _ in range(N):
        arr = list(input().split())
        tree[int(arr[0])] = arr[1]

    print(f'#{tc}', end=' ')
    inorder(1, N)   # root = 1
    print()

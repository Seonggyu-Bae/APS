# v: 현재 정점의 번호
def inorder(v, N):
    # 중위순회란?
    # 왼쪽 서브트리에서 작업을 끝내고 오른쪽 서브트리 작업 시작하기전에 현재 정점에서 작업
    global cnt

    # 우리가 원하는 정점까지만 가야함 아니면 무한정 돌아버림
    if v > N:  # 만약 정점이 최대 정점보다 크면 아무것도 하지 마라
        return
    else:
        # 완전 이진트리이기 때문에 왼쪽 서브트리의 번호는 현재 정점 * 2
        inorder(v * 2, N)

        tree[v] = cnt
        cnt += 1

        # 완전 이진트리이기 때문에 오른쪽 서브트리의 번호는 현재 정점 * 2 + 1
        inorder(v * 2 + 1, N)


# 크기 N인 완전 이진트리 만들기
T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    # 이진 트리는 어떻게 만들까?
    # 완전 이진트리는 배열로 만들면 편하다.
    cnt = 1
    tree = [None] * (N + 1)

    inorder(1, N)
    print(tree)

# T = 1 N =6
#Tree = [None, 4, 2, 6, 1, 3, 5]
"""
                    4
            2                6
        1       3        5   


"""


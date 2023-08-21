"""
첫 줄에는  트리의 정점의 총 수 V가 주어진다.
그 다음 줄에는 V-1개 간선이 나열된다.
간선은 그것을 이루는 두 정점으로 표기된다.
간선은 항상 부모 자식 순서로 표기된다.
간선은 부모 정점 번호가 작은 것 부터 나열되고, 부모 정점이 동일하다면 자식 정점 번호가 낮은 것부터 나열된다.

13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
"""


def preorder(n):
    if n:  # 존재하는 정점이면
        print(n, end=' ')  # visit(n)
        preorder(ch1[n])  # 왼쪽 서브트리로 이동
        preorder(ch2[n])  # 오른쪽 서브트리로 이동


V = int(input())  # 정점 갯수 = 마지막 정점 번호
E = V - 1  # tree 의 간선 수 = 정점 수 -1
edges = list(map(int, input().split()))

# 부모를 인덱스로 자식을 저장
ch1 = [0] * (V + 1)
ch2 = [0] * (V + 1)

# 자식을 인덱스로 부모 저장
par = [0] * (V + 1)

for i in range(E):
    p, c = edges[i * 2], edges[i * 2 + 1]
    if ch1[p] == 0:  # 자식1이 아직 없으면
        ch1[p] = c
    else:
        ch2[p] = c

    par[c] = p  # 자식을 인덱스로 부모 저장

# 루트 찾기는 증요하다.
root = 1
while par[root] != 0:
    root += 1


preorder(root)
print()
preorder(1)

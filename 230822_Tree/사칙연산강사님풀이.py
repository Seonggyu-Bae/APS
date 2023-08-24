# 후위 순회 결과를 반환하는 함수를 작성
# 노드가 값이라면 그대로 반환
# 노드가 연산자라면 왼쪽자식 결과와 오른쪽 자식 결과를 연산해서 반환할것임
def postorder(v):
    if type(tree[v][0]) == 'int':
        return tree[v][0]
    elif str(tree[v][0]) not in '+-*/':
        return tree[v][0]

    left = postorder(tree[v][1])
    right = postorder(tree[v][2])

    if tree[v][0] == '+':
        return left + right
    elif tree[v][0] == '-':
        return left - right
    elif tree[v][0] == '*':
        return left * right
    else:
        return left / right


for tc in range(1, 11):
    N = int(input())

    tree = [[0] * 3 for _ in range(N + 1)]
    for _ in range(N):
        node = input().split()
        node_num = int(node[0])
        if node[1] in '+-*/':  # 연산자면
            tree[node_num][0] = node[1]
            tree[node_num][1] = int(node[2])
            tree[node_num][2] = int(node[3])
        else:  # 피연산자
            tree[node_num][0] = int(node[1])

    result = int(postorder(1))
    print(result)

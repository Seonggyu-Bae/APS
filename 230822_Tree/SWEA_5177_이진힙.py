def bmh_push(data):
    global heap_pointer
    # 이진 최소힙은 아래와 같은 특징을 가진다.
    # 항상 완전 이진 트리를 유지하기 위해 마지막 노드 위에 새 노드를 추가한다.
    # 부모 노드의 값 < 자식 노드의 값을 유지한다.
    # 새로 추가된 노드의 값이 조건에 맞지 않는 경우, 조건을 만족할 때 까지 부모 노드와 값을 바꾼다.
    # 노드 번호는 루트가 1번, 왼쪽에서 오른쪽으로, 더 이상 오른쪽이 없는 경우 다음 줄로 1씩 증가한다.
    my_bmh[heap_pointer] = data
    child = heap_pointer
    parent = child // 2

    while my_bmh[child] < my_bmh[parent] and parent > 0:
        my_bmh[child], my_bmh[parent] = my_bmh[parent], my_bmh[child]
        child = parent
        parent = child // 2

    heap_pointer += 1


def last_node_parent_sum():
    temp = len(my_bmh) - 1
    parent_sum = 0

    while temp > 1:
        temp = temp//2
        parent_sum += my_bmh[temp]

    return parent_sum


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    heap_pointer = 1

    my_bmh = [0] * (N + 1)

    for num in numbers:
        bmh_push(num)

    print(f'#{tc} {last_node_parent_sum()}')

# 힙 만들어서 삽입하는 연산

# 최소 힙에 사용하는 푸쉬
def heap_push(data):
    global heap_pointer
    # 완전이진트리 유지를 위해
    # 이진트리 마지막(힙포인터위치)에 넣어주고
    # 방금 넣은 요소가 heap 조건(부모보다 작은지)을 만족하는지 확인
    # 아니면 바꿔주기
    heap[heap_pointer] = data
    child = heap_pointer
    parent = child // 2

    while parent > 0 and heap[child] < heap[parent]:
        heap[child], heap[parent] = heap[parent], heap[child]
        child = parent
        parent = child // 2
    heap_pointer += 1


def heap_pop():
    pass


# heap 역할을 할 이진트리를 배열(리스트)로 만들자
heap = [0] * 101
# 힙의 어느 위치에 요소가 들어가야하는지 알려주는 변수가 필요함
heap_pointer = 1

heap_push(4)
heap_push(5)
heap_push(6)
heap_push(2)
heap_push(3)
heap_push(22)
heap_push(10)
heap_push(11)
heap_push(30)
heap_push(7)

print(heap)

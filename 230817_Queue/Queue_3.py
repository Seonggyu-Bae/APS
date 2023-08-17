def enq(data):
    global rear
    global front
    """ 큐가 다 차있을때 제일 먼저 들어온놈에다가 덮어쓰는 코드
    if (rear+1)%cQsize == front:
        front =  (front+1)%cQsize
    rear = (rear+1)%cQsize
    cQ[rear] = data
    """

    if (rear + 1) % cQsize == front:
        print('cQ is Full')
    else:
        rear = (rear + 1) % cQsize
        cQ[rear] = data


def deq():
    global front
    front = (front + 1) % cQsize
    return cQ[front]


cQsize = 4
cQ = [0] * 4  # 원형 큐
front, rear = 0, 0

enq(1)
enq(2)
enq(3)
print(deq())
print(deq())
enq(4)

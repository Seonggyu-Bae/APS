def enQ(data):
    global rear
    if rear == Q_size - 1:  # 큐가 다 차있으면
        print("Queue is Full")
    else:
        rear += 1
        my_Q[rear] = data


def deQ():
    global front
    global rear
    if front == rear:  # 비어 있으면
        print("Queue is Empty")
        return -1
    else:
        front += 1
        return my_Q[front]


Q_size = 3
my_Q = [0] * Q_size
rear = -1
front = -1

enQ(1)
enQ(2)

print(deQ())
print(my_Q)

while front != rear:  # 큐가 비어있지 않으면
    front += 1
    print(my_Q[front])

from collections import deque

q = deque()

for i in range(10000000):
    q.append(i)

for i in range(10000000):
    print(q.popleft())

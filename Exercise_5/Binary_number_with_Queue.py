from collections import deque
def binary_with_quque(num):
    q=deque()
    q.appendleft('1')
    for i in range(num):
        front=q[-1]
        print(front)
        q.appendleft(front+'0')
        q.appendleft(front+'1')
        q.pop()
binary_with_quque(10)
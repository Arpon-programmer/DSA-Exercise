import threading
import time
from collections import deque
orders=deque()
def place_order(list):
    for i in list:
        orders.appendleft(i)
        print(f'Taking order for : {i}')
        time.sleep(2)
def serve_order():
    time.sleep(1)
    while orders:
        print(f'Serving : {orders.pop()}')
        time.sleep(2)
list = ['pizza','samosa','pasta','biryani','burger']
t=time.time()
t1=threading.Thread(target=place_order, args=(list,))
t2=threading.Thread(target=serve_order)
t1.start()
t2.start()      #Takes 11 seconds
t1.join()
t2.join()
print(time.time()-t)
# t=time.time()
# place_order(list)
# serve_order()         #Takes 21 seconds
# print(time.time()-t)
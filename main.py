from QueueSLL import *

if __name__ == '__main__':
    Queue = Queue(10)
    Queue.enqueue(2)
    Queue.enqueue(14)
    Queue.enqueue(43)
    Queue.dequeue()
    Queue.display()


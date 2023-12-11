from SLL import *


class Queue:
    def __init__(self, cap):
        self.items = SLinkedList()
        self.size = 0
        self.capacity = cap

    def enqueue(self, data):
        if self.size == self.capacity:
            print("Queue is full.")
        else:
            self.items.start_item(data)
            self.size += 1

    def dequeue(self):
        if self.size == 0:
            print("Queue is empty.")
        else:
            self.items.remove_end()
            self.peek()
            self.size -= 1

    def display(self):
        self.items.display()

    def peek(self):
        return self.items.tail.data

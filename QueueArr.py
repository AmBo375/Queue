class Queue:
    def __init__(self, cap):
        self.items = []
        self.size = 0
        self.capacity = cap

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, data):
        if self.is_full():
            print("Queue is full.")
        else:
            self.items.append(data)
            self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            self.items.pop(0)
            self.size -= 1

    def display(self):
        for i in range(0, self.size):
            print(self.items[i])

    def peek(self):
        return self.items[-1]

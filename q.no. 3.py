class circularQueue:
    def __init__(self):
        self.queue = []

    # Add an element
    def enqueue(self, item):
        self.queue.append(item)
    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)
    # Display the queue
    def display(self):
        print(self.queue)
    def size(self):
        return len(self.queue)
    def front(self):
        temp = []
        temp.append(self.dequeue())

        print("the front element is :", temp[0])
    def rear(self):
        print("the rear element is: ", self.queue[-1])
q = circularQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.display()
q.dequeue()
print("After removing an element")
q.display()
q.front()
q.rear()
q.dequeue()
q.enqueue(1)
print("after adding element")
q.front()
q.rear()
q.display()




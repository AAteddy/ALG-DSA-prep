# demonstration of designing a Circular Queue in Array
# One of the benefits of the circular queue is that we can make use of the spaces in front of the queue.


class MyCircularQueue:
    # MyCircularQueue(k) Initializes the object with the size of the queue to be k.
    def __init__(self, k: int):
        self.size = 0
        self.max_size = k
        self.front = 0
        self.rear = -1
        self.array = [0] * k

    def enQueue(self, value: int) -> bool:
        # Inserts an element into the circular queue. Return true if the operation is successful.
        if self.isFull():
            return False

        self.rear = (self.rear + 1) % self.max_size
        self.array[self.rear] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        # Deletes an element from the circular queue. Return true if the operation is successful.
        if self.isEmpty():
            return False

        self.front = (self.front + 1) % self.max_size
        self.size -= 1
        return True

    def Front(self) -> int:
        # int Front() Gets the front item from the queue. If the queue is empty, return -1.
        if self.isEmpty():
            return -1
        return self.array[self.front]

    def Rear(self) -> int:
        # int Rear() Gets the last item from the queue. If the queue is empty, return -1.
        if self.isFull():
            return -1
        return self.array[self.rear]

    def isEmpty(self) -> bool:
        #  Checks whether the circular queue is empty or not.
        return self.size == 0

    def isFull(self) -> bool:
        # Checks whether the circular queue is full or not.
        return self.max_size == self.size


if __name__ == "__main__":
    # Your MyCircularQueue object will be instantiated and called as such:
    obj = MyCircularQueue(10)
    param_1 = obj.enQueue(1)
    param_2 = obj.deQueue()
    param_3 = obj.Front()
    param_4 = obj.Rear()
    param_5 = obj.isEmpty()
    param_6 = obj.isFull()

# demonstration of designing a Circular Queue in Linked list


class ListNode:
    def __init__(self, val, nxt, prev):
        self.value = val
        self.next = nxt
        self.prev = prev


class MyCircularQueue:
    def __init__(self, k: int):
        self.space = k
        self.left = ListNode(0, None, None)
        self.right = ListNode(0, None, self.left)
        self.left.next = self.right

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        curr = ListNode(value, self.right, self.right.prev)
        self.right.prev.next = curr
        self.right.prev = curr
        self.space -= 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.left.next = self.left.next.next
        self.left.next.prev = self.left
        self.space += 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.left.next.value

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.right.prev.value

    def isEmpty(self) -> bool:
        if self.left.next == self.right:
            return True

    def isFull(self) -> bool:
        if self.space == 0:
            return True

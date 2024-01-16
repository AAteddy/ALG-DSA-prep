# demonstration of a Linked List implementation.
# Insert/Delete element at Start - O(1)
# Insert/Delete an element at End - O(n)
# Insert element in Middle - O(n)
# Search for an element in list - O(n)


class Node:
    def __init__(self, data=None, nxt=None):
        self.data = data
        self.nxt = nxt


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        newNode = Node(data, self.head)
        self.head = newNode

    def insert_at_end(self, data):
        if not self.head:
            self.head = Node(data, None)
            return

        currNode = self.head
        while currNode.nxt:
            currNode = currNode.nxt

        currNode.nxt = Node(data, None)

    def insert(self, data):
        if not self.head:
            self.head = Node(data, self.head)
        else:
            currNode = self.head
            while currNode.nxt:
                currNode = currNode.nxt

            currNode.nxt = Node(data, None)

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        currNode = self.head
        llstr = ""

        while currNode:
            llstr += str(currNode.data) + "-->"
            currNode = currNode.nxt

        print(llstr)


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_begining(4)
    ll.insert_at_begining(89)
    ll.insert_at_begining(13)
    ll.insert_at_end(10)
    ll.insert_at_end(2)
    ll.insert(260)
    ll.insert(45)
    ll.insert(7)
    ll.print()

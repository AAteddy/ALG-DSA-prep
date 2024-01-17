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
        """Insert a new node at the beginning of the list."""
        newNode = Node(data, self.head)
        self.head = newNode

    def insert_at_end(self, data):
        """Insert a new node at the end of the list."""
        if not self.head:
            self.head = Node(data, None)
            return

        currNode = self.head
        while currNode.nxt:
            currNode = currNode.nxt

        currNode.nxt = Node(data, None)

    def insert(self, data):
        """Insert a new node to a linked list."""
        if not self.head:
            self.head = Node(data, self.head)
        else:
            currNode = self.head
            while currNode.nxt:
                currNode = currNode.nxt

            currNode.nxt = Node(data, None)

    def reverseList(self):
        """Reverse a linked list in iterative approach"""
        prev = None
        current = self.head

        while current:
            next_node = current.nxt
            current.nxt = prev
            prev = current
            current = next_node
        self.head = prev

    def print(self):
        """Print all elements in the linked list."""
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
    ll.reverseList()
    ll.print()

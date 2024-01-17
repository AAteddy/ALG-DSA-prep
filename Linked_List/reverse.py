# demonstration of a Reverse Linked List solution
# Problem:
# Given the head of a singly linked list, reverse the list, and return the reversed list.
# Solution: Iterative approach
# Two Pointer technique
# We start with a prev pointer set to None and a current pointer set to the head of the list.
# We then enter a loop where we save the next node, reverse the link by setting current.next to prev, and move the prev and current pointers one step forward.
# When we reach the end of the list, we set the head of the list to prev, which is now the last node we visited (and therefore the new head of the reversed list).
# Example:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class llist:
def reverseList(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

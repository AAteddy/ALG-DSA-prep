# demonstration of a Linked List Cycle.
# A Circular linked list is a singly linked list where the last node points back to the first node.
# Problem:
# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list
# that can be reached again by continuously following the next pointer
# Return true if there is a cycle in the linked list. Otherwise, return false.
# Example:
# Input: head = [3,2,0,-4], pos = 1
# Output: true


def hasCycle(head):
    fast, slow = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

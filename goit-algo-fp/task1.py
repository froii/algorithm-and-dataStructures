

from typing import Optional


class Node:
    def __init__(self, value):
        self.value = value
        self.next: Optional['Node'] = None


class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None

    def append(self, value) -> None:
        if not self.head:
            self.head = Node(value)
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = Node(value)

    def reverse(self) -> None:
        cur = self.head
        prev = None

        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        self.head = prev

    def sort(self) -> None:
        self.head = self._merge_sort(self.head)

    def _merge_sort(self, head) -> Optional[Node]:
        if not head or not head.next:
            return head

        mid = self._get_middle(head)
        mid.next, mid_next = None, mid.next  # type: ignore

        left = self._merge_sort(head)
        right = self._merge_sort(mid_next)

        return self._merge(left, right)

    def _get_middle(self, head) -> Optional[Node]:
        if not head:
            return head

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def _merge(self, left, right) -> Optional[Node]:
        if not left:
            return right
        if not right:
            return left

        if left.value <= right.value:
            result = left
            result.next = self._merge(left.next, right)
        else:
            result = right
            result.next = self._merge(left, right.next)

        return result


def merge_sorted_lists(list1: LinkedList, list2: LinkedList) -> LinkedList:
    dummy = Node(0)
    tail = dummy

    head1 = list1.head
    head2 = list2.head

    while head1 and head2:
        if head1.value <= head2.value:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next

    tail.next = head1 if head1 else head2

    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list

from collections.abc import Iterable


class ListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)


class LinkedList(Iterable):
    def __init__(self):
        self.head = None
        self._current = None

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '[' + ', '.join(nodes) + ']'

    def __iter__(self):
        self._current = self.head
        return self

    def __next__(self):
        if self._current is None:
            raise StopIteration
        element = self._current
        self._current = self._current.next
        return element

    def prepend(self, data):
        self.head = ListNode(data=data, next=self.head)

    def append(self, data):
        if not self.head:
            self.head = ListNode(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(data=data)

    def find(self, key):
        curr = self.head
        while curr and curr.data != key:
            curr = curr.next
        return curr

    def remove(self, key):
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next

        # Unlink it from the list

        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None

    def reverse(self):
        curr = self.head
        prev_node = None
        next_node = None
        while curr:
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node
        self.head = prev_node


if __name__ == "__main__":
    linked_list = LinkedList()
    for value in range(20):
        linked_list.append(value)

    for node in linked_list:
        print(node)

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        print(self.val)


class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = Node(0)

    def print_ll(self):
        curr = self.head
        for _ in range(self.size):
            print(curr.val)
            curr = curr.next


    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        curr = self.head
        for _ in range(index+1):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index < 0:
            index = 0
        self.size += 1
        pred = self.head
        for _ in range(index):
            pred = pred.next
        to_add = Node(val)
        to_add.next = pred.next
        pred.next = to_add

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        self.size -= 1
        pred = self.head
        for _ in range(index):
            pred = pred.next
        pred.next = pred.next.next
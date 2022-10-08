# https://leetcode.com/explore/learn/card/linked-list/209/singly-linked-list/1287/
# https://leetcode.com/problems/design-linked-list/
# https://www.geeksforgeeks.org/linked-list-set-2-inserting-a-node/?ref=lbp


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


class SimpleLinkedList:
    def __init__(self):
        self.head = None

    def add_item_at_the_top_aka_push_item(self, data):
        new = Node(data)
        new.next = self.head        # новый элемент ПРЕДШЕСТВУЕТ голове списка    ("после нового следует голова списка")
        self.head = new             # голова теперь - это НОВЫЙ элемент

    def insert_new_item_after_specific_existed_item(self, new_data, existed_item):
        new = Node(new_data)
        new.next = existed_item.next        # новый указывает на того , кто идет после существующего. т о на "того" указывают теперь ДВА объекта (сущ-ий и новый)
        existed_item.next = new             # существующий теперь УКАЗЫВАЕТ на новый, новый идет ПОСЛЕ существующего

    def get_tail(self):
        tail = self.head

        while tail.next:
            tail = tail.next
        return tail

    def get_tail_data(self):
        tail = self.head

        while tail.next:
            tail = tail.next
        return tail.data

    def insert_node_at_the_end(self, new_data):
        new = Node(new_data)

        # find end of the list using existed method
        tail = self.get_tail()
        tail.next = new

    def print_items_and_its_data(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def delete_first_item_aka_head(self):
        new_head = self.head.next               # новая голова - та, на кого указвает текущая
        self.head = new_head                    # КОРОНУЕМ нову голову

    def delete_item(self, item4delete):
        suspended = self.head
        while suspended != item4delete:
            previous = suspended
            suspended = suspended.next

        new_pointer = suspended.next            # определеяем на кого указывает УДАЛЯЕМЫЙ
        previous.next = new_pointer

# with size calc
class LinkedListWithSizeCounting:
    def __init__(self):
        self.head = Node()
        self.size = 0

    def add_item(self, data):
        pass


    def get_item_by_index(self, index):
        pass


# ToDo: Approach 2: Doubly Linked List https://leetcode.com/problems/design-linked-list/solution/

class DoubleLinkedList:
    pass





if __name__ == '__main__':
    temp = SimpleLinkedList()
    for i in range(5):
        temp.add_item_at_the_top_aka_push_item(i)
    temp.insert_node_at_the_end(42)
    temp.print_items_and_its_data()
    # print(temp.get_tail_data())
    temp.delete_first_item_aka_head()
    print('-')
    temp.print_items_and_its_data()

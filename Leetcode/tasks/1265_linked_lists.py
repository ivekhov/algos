class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_next(self):
        return self.next

    def print_value(self):
        print(self.data)

    def __repr__(self):
        return str(self.data)


class LinkedList:
    def __init__(self, node):
        self.head = node

    def insert_at_beginning(self, node):
        node.next = self.head
        self.head = node

    def __repr__(self):
        s = ''
        tmp = self.head
        while tmp:
            s = s + str(tmp.data) + '-->'
            tmp = tmp.next
        return s

    def get_arr(self):
        arr = []
        tmp = self.head
        while tmp:
            arr.append(tmp)
            tmp = tmp.next
        return arr


ll = LinkedList(Node(1))
ll.insert_at_beginning((Node(2)))
ll.insert_at_beginning((Node(3)))
# print(ll.get_arr())


# 1265 solution

def print_in_reverse(head):
    arr = []
    tmp = head
    while tmp:
        arr.append(tmp)
        tmp = tmp.get_next()
    [el.print_value() for el in arr[::-1]]


# print_in_reverse(ll.head)

# 1265
def print_in_reverse_rec(head):
    next = head.get_next()
    if not next:
        head.print_value()
        return


    else:
        print_in_reverse_rec(next)

    head.print_value()
    return


# print_in_reverse_rec(ll.head)

#################

def print_arr_rec(arr):

    if len(arr) < 1:
        return

    print(arr[0])
    print_arr_rec(arr[1:])


# print_arr_rec([1, 2, 3, 4, 5])

arr = [1, 2, 3, 42, 11, -1, 0, 9999]


def get_max(arr):

    if len(arr) <= 1:
        return arr

    if len(arr) == 2:
        return arr[0] if arr[0] > 1 else arr[1]

    sub_max = get_max(arr[1:])

    return arr[0] if arr[0] > sub_max else sub_max


print(get_max(arr))

############ Finish ##########

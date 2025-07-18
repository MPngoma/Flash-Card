class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linked_List:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value,end="->")
            temp = temp.next
        return "\nDone"

    def append(self,value):
        if self.length > 0:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(value)
            self.tail = temp.next
            self.length += 1

        else:
            node = Node(value)
            self.head = node
            self.tail = node
            self.length = 1

    def pop(self):
        # when the list is empty
        if self.length == 0:
            return False
        pre = self.head
        temp = pre
        # when there is one item
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return True
        # when there is multiple
        else:
            while pre.next is not None:
                pre = pre.next
                if pre.next is not None:
                    temp = temp.next

            temp.next = None
            self.tail = temp
            self.length -= 1
            return pre.value # return the whole node: I am returning value just to visualize it

    def prepend(self,value):
        # when LL is empty
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        # when there is items in the LL
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        # when the LL starts empty
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp.value  # return the whole node: I am returning value just to visualize it

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp # return the whole node: return value just to visualize it

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if self.length == 0:
            self.prepend(value)
        if index == self.length:
            self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if self.length == 0:
            return False
        if index == self.length - 1:
            self.pop()
        if self.length == 1 or index == 0:
            self.pop_first()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp.value

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp.next
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return True

    def find_middle_node(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow.value

    def binary_to_decimal(self):
        current = self.head
        total = 0
        while current is not None:
            total = (total * 2) + current.value
            current = current.next
        return total

    def reverse_between(self, n1, n2):
        if not self.head:
            return None
        prev = self.head
        current = prev.next
        i = 0
        while i < n2 - n1:
            to_move = current.next
            current.next = to_move.next
            to_move.next = prev.next
            prev.next = to_move
            i += 1

    def pair_swap(self):
        if not self.length <= 1:
            return

        prev = self.head
        current = prev.next

        while current:
            prev.next = current.next
            current = prev
            prev = prev.next
            current = prev.next







my_ll = Linked_List(1)
my_ll.append(2)
my_ll.append(3)
my_ll.append(4)
my_ll.append(5)
my_ll.print_list()
my_ll.reverse_between(2, 4)
print("\n")
my_ll.print_list()
print("\n")
my_ll.pair_swap()
my_ll.print_list()
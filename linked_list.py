class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def load(self, items):
        for item in items:
            self.append(item)

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def search(self, target):
        current = self.head
        index = 0

        while current:
            if current.data == target:
                return index
            current = current.next
            index += 1

        return -1

    def delete(self, target):
        if self.head is None:
            return False

        if self.head.data == target:
            self.head = self.head.next
            return True

        prev = self.head
        current = self.head.next

        while current:
            if current.data == target:
                prev.next = current.next
                return True
            prev = current
            current = current.next

        return False

    def size(self):
        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next

        return count

    def print_list(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

linked_list = LinkedList()

# Input data.
linked_list.load([])

linked_list.print_list()

# Input the value you want to find.
target = 

print(linked_list.search(target))

print(linked_list.size())
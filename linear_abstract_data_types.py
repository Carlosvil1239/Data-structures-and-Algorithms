# Linear Abstract Data Types: stacks, queues and linked lists

class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0


class SinglyNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, value):
        new_node = SinglyNode(value)
        new_node.next = self.head
        self.head = new_node

    def insert_back(self, value):
        new_node = SinglyNode(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    def search(self, value):
        current = self.head

        while current is not None:
            if current.value == value:
                return True
            current = current.next

        return False

    def delete(self, value):
        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        current = self.head

        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

    def print_list(self):
        current = self.head

        while current is not None:
            print(current.value, end=" -> ")
            current = current.next

        print("None")


class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_front(self, value):
        new_node = DoubleNode(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_back(self, value):
        new_node = DoubleNode(value)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def delete(self, value):
        current = self.head

        while current is not None:
            if current.value == value:
                if current.prev is not None:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next is not None:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                return

            current = current.next

    def print_forward(self):
        current = self.head

        while current is not None:
            print(current.value, end=" <-> ")
            current = current.next

        print("None")

    def print_backward(self):
        current = self.tail

        while current is not None:
            print(current.value, end=" <-> ")
            current = current.prev

        print("None")


if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    print(stack.pop())

    queue = Queue()
    queue.enqueue("A")
    queue.enqueue("B")
    print(queue.dequeue())

    sll = SinglyLinkedList()
    sll.insert_back(1)
    sll.insert_back(2)
    sll.insert_front(0)
    sll.print_list()

    dll = DoublyLinkedList()
    dll.insert_back(5)
    dll.insert_back(6)
    dll.insert_front(4)
    dll.print_forward()
    dll.print_backward()

from linkedList import Element
from linkedList import LinkedList


class LinkedList(LinkedList):
    def __init__(self, value):
        super().__init__(value)

    def insert_first(self, new_element):
        new_element.next = self.head
        self.head = new_element

    def delete_first(self):
        if self.head:
            current_head = self.head
            self.head = self.head.next
        else:
            current_head = None
        return current_head


class Stack():
    def __init__(self, top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        self.ll.insert_first(new_element)

    def pop(self):
        return self.ll.delete_first()


if __name__ == "__main__":

    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)
    e4 = Element(4)

    stack = Stack(e1)
    stack.push(e2)
    stack.push(e3)
    print(stack.pop().value)
    print(stack.pop().value)
    print(stack.pop().value)
    print(stack.pop())
    stack.push(e4)
    print(stack.pop().value)

"L=inked List implementation."


class Element(object):
    "Linked list element."

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    "Linked list object."

    def __init__(self, head=None):
        self.head = head
        self.size = 0
        self.iterCount = 1

    def __len__(self):
        return self.size

    def __contains__(self, value):
        current = self.head
        while current and current.value != value:
            current = current.next
        return current is not None

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterCount > self.size:
            raise StopIteration
        else:
            current = self.get_position(self.iterCount)
            self.iterCount += 1
            return current.value

    def append(self, new_element):
        self.size += 1
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None

    def insert(self, new_element, position):
        counter = 1
        current = self.head
        if position == 1:
            self.head = new_element
            self.head.next = current
            return

        while current and counter < position:
            if counter == position - 1:
                new_element.next = current.next
                current.next = new_element
            current = current.next
            counter += 1

    def delete(self, value):
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next


if __name__ == "__main__":

    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)
    e4 = Element(4)

    ll = LinkedList(e1)
    ll.append(e2)
    ll.append(e3)

    print(ll.head.next.next.value)
    print(ll.get_position(3).value)

    ll.insert(e4, 3)
    print(ll.get_position(3).value)

    ll.delete(1)
    print(ll.get_position(1).value)
    print(ll.get_position(2).value)
    print(ll.get_position(3).value)

    for value in ll:
        print('value: {}'.format(value))

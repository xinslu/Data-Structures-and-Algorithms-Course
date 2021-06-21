class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        current = self.head
        count = 1
        while current.next and count != position:
            current = current.next
            count += 1
        else:
            return current
        return None

    def insert(self, new_element, position):
        current = self.head
        count = 1
        while current.next and count != (position - 1):
            current = current.next
            count += 1
        else:
            prev_node = current
            current = current.next
            prev_node.next = new_element
            new_element.next = current

    def delete(self, value):
        current = self.head
        if current.value == value:
            self.head = current.next
        while current.next != None:
            if current.next.value == value:
                prev_node = current
                prev_node.next = current.next
            current = current.next

    def display(self):
        current = self.head
        elems = [current.value]
        while current.next != None:
            current = current.next
            elems.append(current.value)
        print(elems)


e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

ll.insert(e4, 3)
ll.display()
# Test delete
ll.delete(1)
# Should print 2 now

print(ll.get_position(1).value)
# Should print 4 now
print(ll.get_position(2).value)
# Should print 3 now
print(ll.get_position(3).value)

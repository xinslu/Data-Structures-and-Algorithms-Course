"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self,value):
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
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        current=self.head
        count=1
        while current.next and count!=position:
            current=current.next
            count+=1
        else:
            return current
        return None
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        current=self.head
        count=1
        while current.next and count!=(position-1):
            current=current.next
            count+=1
        else:
            prev_node=current
            current=current.next
            prev_node.next=new_element
            new_element.next=current
    
    
    def delete(self, value):
        """Delete the first node with a given value."""
        current=self.head
        if current.value==value:
            self.head=current.next
        while current.next!=None:
            if current.next.value==value:
                prev_node=current
                prev_node.next=current.next
            current=current.next
    
    def display(self):
        current=self.head
        elems=[current.value]
        while current.next!=None:
            current=current.next
            elems.append(current.value)
        print(elems)

    


e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

ll.insert(e4,3)
ll.display()
# Test delete
ll.delete(1)
# Should print 2 now

print(ll.get_position(1).value)
# Should print 4 now
print(ll.get_position(2).value)
# Should print 3 now
print(ll.get_position(3).value)
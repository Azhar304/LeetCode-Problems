class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None


    # Add at beginning
    def add_beginning(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node


    # Add at end
    def add_end(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp


    # Traverse forward
    def traverse_forward(self):
        if self.head is None:
            return

        temp = self.head
        while temp:
            print(temp.val, end="   ")
            temp = temp.next


    # Traverse backward
    def traverse_backward(self):
        if self.head is None:
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        while temp:
            print(temp.val, end="   ")
            temp = temp.prev


    # Delete from beginning
    def delete_begin(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        self.head = self.head.next
        self.head.prev = None


    # Delete from end
    def delete_end(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.prev.next = None


    # Delete by value
    def delete_val(self, value):
        if self.head is None:
            return

        temp = self.head

        # If head contains value
        if temp.val == value:
            self.delete_begin()
            return

        while temp:
            if temp.val == value:
                if temp.next:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                else:  # last node
                    temp.prev.next = None
                return
            temp = temp.next


    # Reverse list
    def reverse(self):
        if self.head is None:
            return

        temp = None
        curr = self.head

        while curr:
            temp = curr.prev
            curr.prev = curr.next
            curr.next = temp
            curr = curr.prev

        if temp:
            self.head = temp.prev
          

n = DoublyLinkedList()

n.add_beginning(5)
n.add_end(10)
n.add_end(15)
n.add_end(20)
n.add_end(25)
n.add_end(35)
n.add_end(45)
n.add_end(55)
n.add_end(65)

print("\nBefore deletion from start")
n.traverse_forward()

n.delete_begin()
print("\nAfter deletion from start")
n.traverse_forward()

print("\nBefore deletion from end")
n.traverse_forward()
n.delete_end()
print("\nAfter deletion from end")
n.traverse_forward()

print("\nBefore deletion by value")
n.traverse_forward()
n.delete_val(35)
print("\nAfter deletion by value")
n.traverse_forward()

print("\nReversal")
n.reverse()
n.traverse_forward()

print("\nTraverse Backward")
n.traverse_backward()



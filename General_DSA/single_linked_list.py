class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head

        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        

    def delete_begin(self):
        if self.head is None:
            return
        
        self.head= self.head.next

    def delete_end(self):
        if self.head is None:
            return
        
        if self.head.next is None:
            self.head = None
            return
        
        temp = self.head
        while temp.next.next:
            temp = temp.next
        
        temp.next = None

    def delete_value(self, value):
        if self.head is None:
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        
        prev = self.head
        curr = self.head.next

        while curr:
            if curr.data == value:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next




ll = LinkedList()

ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)

ll.insert_begin(5)
print("before deletion")
ll.traverse()
ll.delete_begin()
print("\nafter deletion")
ll.traverse()

ll.delete_end()
print("\ndeletion from end")
ll.traverse()

ll.insert_end(40)
ll.insert_end(50)
ll.insert_end(60)
print("\nbefore deletion")
ll.traverse()
ll.delete_value(50)
print("\nafter deletion")

ll.traverse()
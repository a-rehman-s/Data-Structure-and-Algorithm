class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        
    def append(self,data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
                
    def display(self):
        current = self.head
        while current:
            print(current.data,end=" -> ")
            current = current.next
        print("None")
        
sll = SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.display()   
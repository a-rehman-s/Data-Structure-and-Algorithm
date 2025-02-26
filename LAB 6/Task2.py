class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.head.next = self.head  
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = node
            node.next = self.head  

    def delete(self, key):
        if self.head is None:
            return

        temp = self.head
        prev = None

        if temp.data == key:
            while temp.next != self.head:
                temp = temp.next
            if self.head == self.head.next:
                self.head = None 
            else:
                temp.next = self.head.next
                self.head = self.head.next
            return

        while temp.next != self.head and temp.data != key:
            prev = temp
            temp = temp.next

        if temp.data == key:
            prev.next = temp.next

    def traverse(self):
        if self.head is None:
            print("List is empty!")
            return
        temp = self.head
        while True:
            print(temp.data, "->", end=" ")
            temp = temp.next
            if temp == self.head:
                break
        print("(Back to head)")

cll = CircularLinkedList()
cll.append(10)
cll.append(20)
cll.append(30)
cll.traverse()  
cll.delete(20)
cll.traverse() 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class UndoRedo:
    def __init__(self):
        self.head = None
        self.current = None

    def add_action(self, action):
        node = Node(action)
        if self.head is None:
            self.head = self.current = node
            node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = node
            node.next = self.head

    def undo(self):
        if self.current is None:
            print("No actions to undo!")
            return
        temp = self.head
        while temp.next != self.current:
            temp = temp.next
        self.current = temp
        print("Undo:", self.current.data)

    def redo(self):
        if self.current:
            self.current = self.current.next
            print("Redo:", self.current.data)

history = UndoRedo()
history.add_action("Type A")
history.add_action("Type B")
history.undo()  
history.redo() 

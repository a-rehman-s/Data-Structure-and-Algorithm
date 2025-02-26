class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class ChatHistory:
    def __init__(self):
        self.head = None
        self.current = None

    def add_message(self, message):
        node = Node(message)
        if self.head is None:
            self.head = self.current = node
            node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = node
            node.next = self.head

    def view_previous(self):
        if self.current is None:
            print("No messages!")
            return
        temp = self.head
        while temp.next != self.current:
            temp = temp.next
        self.current = temp
        print("Previous Message:", self.current.data)

    def view_next(self):
        if self.current:
            self.current = self.current.next
            print("Next Message:", self.current.data)

chat = ChatHistory()
chat.add_message("Hello!")
chat.add_message("How are you?")
chat.view_previous()  
chat.view_next()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class RoundRobinScheduler:
    def __init__(self):
        self.head = None

    def add_process(self, process_id):
        node = Node(process_id)
        if self.head is None:
            self.head = node
            node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = node
            node.next = self.head  

    def execute_processes(self, cycles=3):
        if self.head is None:
            print("No processes available!")
            return
        temp = self.head
        for _ in range(cycles):
            print(f"Executing Process {temp.data}")
            temp = temp.next

scheduler = RoundRobinScheduler()
scheduler.add_process(1)
scheduler.add_process(2)
scheduler.add_process(3)
scheduler.execute_processes(5)

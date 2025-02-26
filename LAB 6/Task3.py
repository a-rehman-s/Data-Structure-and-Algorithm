class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class TaskScheduler:
    def __init__(self):
        self.head = None
        self.current_task = None

    def add_task(self, task_name):
        node = Node(task_name)
        if self.head is None:
            self.head = node
            node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = node
            node.next = self.head 

    def execute_tasks(self, cycles=3):
        if self.head is None:
            print("No tasks available!")
            return
        temp = self.head
        for _ in range(cycles):
            print(f"Executing Task: {temp.data}")
            temp = temp.next

scheduler = TaskScheduler()
scheduler.add_task("Task A")
scheduler.add_task("Task B")
scheduler.add_task("Task C")
scheduler.execute_tasks(5)  

from Node import Node

class Queue:
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0
    
    def enqueue(self,value):
        if self.has_space():
            new_input = Node(value)
            print("Adding "+str(new_input.get_value())+" to queue")
            if self.is_empty():
                self.head = new_input
                self.tail = new_input
            else:
                self.tail.set_next_node(new_input)
                self.tail = new_input
            self.size += 1
        else:
            print("Queue is full!")
            
    def dequeue(self):
        if (not self.is_empty()):
            remove_node = self.head
            print("Removing "+str(remove_node.get_value())+" from the queue")
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.head = remove_node.get_next_node()
            self.size -= 1
            return remove_node.get_value()
        else:
            print("Queue is empty!")
    
    def peek(self):
        if not self.is_empty():
            print(f"Queue head: {self.head.get_value()}")
    
    def is_empty(self):
        return self.size == 0
    
    def has_space(self):
        if self.max_size > self.size:
            return True
        else:
            return False
    
    
    
new_queue = Queue(10)

new_queue.enqueue(1)
new_queue.enqueue(2)
new_queue.enqueue(3)
new_queue.enqueue(4)
new_queue.enqueue(5)
new_queue.enqueue(6)
new_queue.enqueue(7)
new_queue.enqueue(8)
new_queue.enqueue(9)
new_queue.enqueue(10)
new_queue.peek()

new_queue.dequeue()
new_queue.dequeue()
new_queue.dequeue()
new_queue.dequeue()
new_queue.dequeue()
new_queue.dequeue()
new_queue.dequeue()
new_queue.peek()
new_queue.dequeue()
new_queue.dequeue()
new_queue.dequeue()
new_queue.peek()
new_queue.dequeue()
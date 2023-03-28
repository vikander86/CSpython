class Node:
    def __init__(self, value, next_node = None, prev_node = None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node
    
    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_node
    
    def get_prev_node(self):
        return self.prev_node
    
    def set_next_node(self, next_node):
        self.next_node = next_node
    
    def set_prev_node(self, prev_node):
        self.prev_node = prev_node
        
class DoublyLinkedList:
    def __init__(self):
        self.head_node=None
        self.tail_node=None
        
    def add_to_head(self, new_value):
        #create new node
        new_head = Node(new_value)
        current_head = self.head_node
        
        #replace head with new_head node
        if current_head is not None:
            new_head.set_next_node(current_head)
            current_head.set_prev_node(new_head)
        self.head_node = new_head
        #if tail is empty, set new head as tail.
        if self.tail_node is None:
            self.tail_node = new_head

    def add_to_tail(self, new_value):
        #create new node
        new_tail = Node(new_value)
        current_tail = self.tail_node
        #replace tail with new_tail node
        if current_tail != None:
            current_tail.set_next_node(new_tail)
            new_tail.set_prev_node(current_tail)
        self.tail_node = new_tail
        #if head is empty, set new tail as head.
        if self.head_node is None:
            self.head_node = new_tail
            
    def remove_head(self):
        #remove head node
        removed_head = self.head_node
        #if head is empty, return none(list empty)
        if removed_head is None:
            return None
        #set next node of head to be the new head
        self.head_node = removed_head.get_next_node()
        
        if self.head_node != None:
            self.head_node.set_prev_node(None)

        #if head is now tail, remove tail pointer
        if removed_head == self.tail_node:
            self.remove_tail()
        return removed_head.get_value()
    
    def remove_tail(self):
        removed_tail = self.tail_node

        if removed_tail == None:
            return None
        
        self.tail_node = removed_tail.get_prev_node()
        if self.tail_node != None:
            self.tail_node.set_next_node(None)
        if removed_tail == self.head_node:
            self.remove_head()
        return removed_tail.get_value()
    
    def remove_by_value(self, value_to_remove):
        node_to_remove = None
        current_node = self.head_node
        while current_node is not None:
            if current_node.get_value() == value_to_remove:
                node_to_remove = current_node
                break
            current_node = current_node.get_next_node()

        #if node with given value does not exist, return None
        if node_to_remove == None:
            return None
        
        #if node with given value is head, call remove_head()
        if node_to_remove == self.head_node:
            self.remove_head()
            
        #if node with given value is tail, call remove_tail()
        elif node_to_remove == self.tail_node:
            self.remove_tail()
        #if node is neither tail nor head, update previous and next pointers of the nodes prev and next nodes.
        else:
            next_node = node_to_remove.get_next_node()
            prev_node = node_to_remove.get_prev_node()
            next_node.set_prev_node(prev_node)
            prev_node.set_next_node(next_node)
        return node_to_remove
    
    def print_list(self):
        current = self.head_node
        while current:
            if current.get_value() is not None:
                print(current.get_value())
            current = current.get_next_node()
        print()
        
    def stringify_list(self):
        string_list = ""
        current_node = self.head_node
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list
            
subway = DoublyLinkedList()
subway.add_to_head("Times Square")
subway.add_to_head("Grand Central")
subway.add_to_head("Central Park")
subway.print_list()

subway.add_to_tail("Penn Station")
subway.add_to_tail("Wall Street")
subway.add_to_tail("Brooklyn Bridge")
subway.print_list()

subway.remove_head()
subway.remove_tail()
subway.print_list()

subway.remove_by_value("Times Square")
subway.print_list()

class Node:
    def __init__(self,value,next_node=None):
        self.value = value
        self.next_node = next_node
    
    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_node
    
    def set_next_node(self, next_node):
        self.next_node = next_node
        
class LinkedList:
    def __init__(self, value):
        self.head_node = Node(value)
    
    def get_head_node(self):
        return self.head_node
    
    def insert_beginning(self,new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
    
    def stringify_list(self):
        #turn list into strings
        string = ""
        current_node = self.head_node
        while current_node:
            if current_node.get_value() != None:
                string += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string
    
    def print_list(self):
        #print list
        current_node = self.head_node
        while current_node:
            print(current_node.get_value())
            current_node = current_node.get_next_node()
    
    def remove_node(self, remove_value):
        #if value is the first node, remove head
        current_node = self.get_head_node()
        if current_node.get_value() == remove_value:
            self.head_node = current_node.get_next_node()
        else:
            #iterate through the list to find our value we want to remove.
            #we will will iterate the list till the value matches that of the currents node next pointer.
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == remove_value:
                    #if found, set the currents next pointer to the next next node. Thus removing the node with the remove value from the list.
                    current_node.set_next_node(next_node.get_next_node())
                    #set current_node to None to stop the loop.
                    current_node = None
                else:
                    current_node = next_node
    
    def swap_nodes(self, value1, value2):
        node1_prev = None
        node2_prev = None
        node1 = self.head_node
        node2 = self.head_node
        
        if value1 == value2:
            print("No swap needed. ${} == ${}").format(value1, value2)


list1 = LinkedList("4")
list1.insert_beginning(5)
list1.insert_beginning(6)
list1.insert_beginning(8)
list1.insert_beginning(11)
list1.insert_beginning(13)
list2 = LinkedList("Test")
list2.insert_beginning("!")
list2.insert_beginning("Dig")
list2.insert_beginning("På")
list2.insert_beginning("Hey")

list1.print_list()
list2.print_list()

# print(list1.stringify_list())
# list1.remove_node(4)
# list1.remove_node(11)
# list1.remove_node(8)
# print(list1.stringify_list())

    
    
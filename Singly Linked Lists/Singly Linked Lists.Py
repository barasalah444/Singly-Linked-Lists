class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None

class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node = SLNode(val)
        new_node.next = self.head
        self.head = new_node
        return self

    def print_values(self):
        curr = self.head            
            print(curr.value)
            curr = curr.next        
        return self

    def add_to_back(self, val):
        if not self.head:
            return self.add_to_front(val)
        
        curr = self.head            
        while curr.next:
            curr = curr.next
        curr.next = SLNode(val)
        return self


my_list = SList()
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()
class Node:

    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    # O(1)
    def insert_at_start(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head, self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        print(f"Update : Added {data} at the start of your list.")

    # O(1)
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        print(f"Update : Added {data} at the end of your list.")

    def insert_before_node(self, data, target_data):
        target_node = self.head

        # Checks if we're not at head and is not equal to target_data
        while target_node and target_node.data != target_data:
            target_node = target_node.next
        
        if target_node is self.head:
            self.insert_at_start(data)
            return
        
        if target_node is None:
            print(f"Error: '{target_data}' node is not found in the list.")
            return
         
        new_node = Node(data)
        new_node.prev = target_node.prev
        new_node.next = target_node
        target_node.prev.next = new_node
        target_node.prev = new_node
    
        


    

     
    
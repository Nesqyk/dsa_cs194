class Node:

    def __init__(self, data):
        self.data = data
        self.next =  None
    

class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def display(self):
        current_node = self.head
        output = []
        while current_node is not None:
            output.append(str(current_node.data))
            current_node = current_node.next
        print(f"List: {'->'.join(output)} -> None")
    
    def insert_at_start(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    
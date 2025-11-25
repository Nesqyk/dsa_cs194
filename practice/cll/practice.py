class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None
    

class CircularLinkedlist:


    def __init__(self):
        self.head = None

    # Initialize a variable for new node.
    # If list is empty make new node point to itself.
    # else:
    # set current node to self.head
    # traverse the list until the last node
    # point current.next to new node
    # make new node point back to the head

    # O(n)
    def append(self, data):
        
        # Initialize new node
        new_node = Node(data)

        # Check if not is empty
        if not self.head:
            # if not point the new node to itself
            new_node.next = new_node
            self.head = new_node
        else:
            # Initialize the current node
            current_node = self.head
            while current_node.next is not self.head:
                # Traverse the node to reach the end
                current_node.next = self.head
            # Point last node the the new node                
            current_node.next = new_node
            # Poitn back the new node to the head.
            new_node.next  = self.head
    
    # Traversing is easy u just have to check whether if its not the head?

    # O(n)
    def traverse(self):
        # check if list is empty
        if not self.head:
            # List is empty.
            print("Circular Linkedlist is Empty")
            return
        # iniitalize current head
        current = self.head
        
        # traversal
        while True:    
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break

# Driver Code:
circular_list = CircularLinkedlist()
circular_list.append(1)
circular_list.append(2)
circular_list.append(3)
            
# %%

class Node:
    def __init__(self, data= None, next=None, prev= None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0
        self.tail = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            print(f" -> Added '{data}' in an empty list.")
        else:
            self.tail.next = new_node   
            new_node.prev = self.tail   

            self.tail = new_node       
            
            print(f" -> Added '{data}' at the end of the list")  
    
    # -- Forward Traversal -- (Head to Tail)
    def traverse_forward(self):
        current = self.head
        output = []
        while current:
            output.append(str(current.data))
            current = current.next
        print(" <-> ".join(output) + " -> None\n")

    def traverse_backward(self):
        current = self.tail
        print("Backward Traversal (Tail to Head):")
        output = []
        while current:
            output.append(str(current.data))
            current = current.prev
        print("None <- " + " <->".join(output) + "\n")
    
    def insert_at_start(self ,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            print(f" -> Added '{data} in an empty list.")
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            print(f" -> Added '{data}' at the start of the list.") 

    
    def inset_after_node(self, target_data, data):
        target_node = self.head
        while target_node and target_node.data != target_data:
            target_node = target_node.next
        
        if target_node is None:
            print(f"Error: '{target_data}' node is not found in the list.")
            return
        if target_node == self.tail:
            self.insert_at_end(data)
            return
        
        new_node = Node(data)
        new_node.next = target_node.next
        new_node.prev = target_node
        target_node.next.prev = new_node
        target_node.next = new_node

        print(f" -> Added '{data}' after '{target_data}' node.") 

    def insert_before_node(self, target_data, data):
        target_node = self.head
        while target_node and target_node.data != target_data:
            target_node = target_node.next
        
        if target_node == self.head:
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
        print(f" -> Added '{data}' before '{target_data}' node.") 
    
    def delete_at_start(self):
        if self.head is None:
            return
        
        deleted_data = self.head.data

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        
        print(f" -> Deleted Head: '{deleted_data}'.")

    def delete_at_end(self):
        if self.tail is None:
            return
        
        deleted_data = self.tail.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        
        else:
            self.tail = self.tail.prev 
            self.tail.next = None     
            
        print(f" -> Deleted Tail: '{deleted_data}'")
    
    def delete_after_node(self, target_data): 
        target_node = self.head 

        while target_node and target_node.data != target_data: 
            target_node = target_node.next 

        if target_node is None: 
            print(f"Error: Target node '{target_data}' is not found in the list.") 
            return 

        node_to_delete = target_node.next 
        if node_to_delete is None: 
            print(f"Error: No node exists after '{target_data}.'") 
            return 

        deleted_data = node_to_delete.data       

        if node_to_delete == self.tail: 
            self.delete_at_end() 
            return 

        target_node.next = node_to_delete.next 
        node_to_delete.next.prev = target_node 
        node_to_delete.next = None 
        node_to_delete.prev = None 

        self.count -= 1 

        print(f" -> Deleted node '{deleted_data}' after '{target_data}'.")

    # Activit 1.

    def delete_before_node(self, target_data):
        target_node = self.head

        while target_node and target_node.data != target_data: 
            target_node = target_node.next 

        if target_node is None: 
            print(f"Error: Target node '{target_data}' is not found in the list.") 
            return 

        node_to_delete = target_node.prev 
        if node_to_delete is None: 
            print(f"Error: No node exists after '{target_data}.'") 
            return 

        deleted_data = node_to_delete.data       

        if node_to_delete == self.head:
            self.head = target_node
            self.head.prev = None
        else:
            node_to_delete.prev.next = target_node
            target_node.prev = node_to_delete.prev

        node_to_delete.next = None
        node_to_delete.prev = None
        self.count -= 1 

        print(f" -> Deleted node '{deleted_data}' before '{target_data}'.")


# --- Activity 2: Testing ---
doubly = DoublyLinkedList()

# 1. Setup (10 to 50)
doubly.insert_at_end(10)
doubly.insert_at_end(20)
doubly.insert_at_end(30)
doubly.insert_at_end(40)
doubly.insert_at_end(50)

print("\n--- Initial Setup ---")
doubly.traverse_forward()
doubly.traverse_backward()

# 2. Test 1: Middle Deletion 
print("\n--- Test 1: Delete before 40 (Middle) ---")
doubly.delete_before_node(40) 
doubly.traverse_forward() # Result: 10 <-> 20 <-> 40 <-> 50

# 3. Test 2: Delegation / Head Deletion
print("\n--- Test 2: Delete before 20 (Head Delegation) ---")
doubly.delete_before_node(20)
doubly.traverse_forward() # Result: 20 <-> 40 <-> 50 (10 is gone!)

# 4. Test 3: Error Case
print("\n--- Test 3: Error Case ---")
doubly.delete_before_node(10)
 
# %%


# %%
class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class CircularDoubly:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # ---------------------------
    # INSERTION OPERATIONS
    # ---------------------------

    def insert_at_start(self, data):
        new_node = Node(data)

        if self.head is None:
            # FIX: Assign individually, cannot unpack single object to 4 vars
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            # Link new node to head
            new_node.next = self.head
            self.head.prev = new_node

            # Link new node to tail
            new_node.prev = self.tail
            self.tail.next = new_node

            # Update head pointer
            self.head = new_node
        
        print(f"-> Added {data} at the start")
        self.size += 1

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            # Link to tail
            new_node.prev = self.tail
            self.tail.next = new_node

            # Link to head (Circular nature)
            new_node.next = self.head
            self.head.prev = new_node

            # Update tail pointer
            self.tail = new_node
        
        print(f"-> Added {data} at the end")
        self.size += 1

    def insert_before_node(self, target_data, data):
        if self.head is None:
            print("-> List is empty.")
            return

        current_node = self.head
        target_node = None # FIX: Use None, not False

        # Search Loop
        while True:
            if current_node.data == target_data: # FIX: Use == not is
                target_node = current_node
                break
            current_node = current_node.next
            if current_node is self.head:
                break
        
        if target_node is None:
            print(f"Could not find {target_data} in your list")
            return

        # Case: Insert before Head
        if target_node is self.head:
            self.insert_at_start(data) # FIX: Pass 'data', not 'target_node'
            return

        # General Case
        new_node = Node(data)
        
        # FIX: Pointer logic was swapped in your version
        new_node.prev = target_node.prev
        new_node.next = target_node

        target_node.prev.next = new_node
        target_node.prev = new_node 
        
        print(f"-> Added {data} before {target_data}")
        self.size += 1

    def insert_after_node(self, target_data, data):
        if self.head is None:
            return

        current_node = self.head
        target_node = None

        while True:
            if current_node.data == target_data: # FIX: Use == not is
                target_node = current_node
                break # FIX: Do not return here, or the code below never runs!
            
            current_node = current_node.next
            if current_node is self.head:
                break
        
        if target_node is None:
            print(f"Could not find {target_data}")
            return
        
        # Case: Insert after Tail
        if target_node is self.tail:
            self.insert_at_end(data) # FIX: Pass 'data'
            return

        # General Case
        new_node = Node(data)

        new_node.next = target_node.next
        new_node.prev = target_node

        target_node.next.prev = new_node
        target_node.next = new_node
        
        print(f"-> Added {data} after {target_data}")
        self.size += 1

    # ---------------------------
    # TRAVERSAL OPERATIONS
    # ---------------------------

    def traverse_forward(self):
        if self.head is None:
            print("List is empty")
            return
        
        curr = self.head
        output = []
        while True:
            output.append(str(curr.data))
            curr = curr.next
            if curr is self.head:
                break
        print("Forward: " + "<->".join(output))

    def traverse_backward(self):
        if self.head is None:
            print("List is empty")
            return
        
        # FIX: Start traversal from Tail for backward
        curr = self.tail 
        output = []
        while True:
            output.append(str(curr.data))
            curr = curr.prev
            if curr is self.tail:
                break
        print("Backward: " + "<->".join(output))

    # ---------------------------
    # DELETION OPERATIONS
    # ---------------------------

    def delete_at_start(self):
        if self.head is None:
            return
        
        if self.head is self.tail: # Only one node
            self.head = None
            self.tail = None
        else:
            new_head = self.head.next
            
            self.tail.next = new_head
            new_head.prev = self.tail
            
            self.head = new_head
        
        self.size -= 1
        print("-> Deleted start node")

    
    """
    New_Tail = Tail.prev      # (Mirror of: New_Head = Head.next)
        
    New_Tail.next = Head      # (Mirror of: Tail.next = New_Head)
    Head.prev = New_Tail      # (Mirror of: New_Head.prev = Tail)
        
    Tail = New_Tail           # (Mirror of: Head = New_Head)
    """
    def delete_at_end(self):
        if self.head is None:
            return
        
        if self.head is self.tail: # Only one node
            self.head = None
            self.tail = None
        else:
            # FIX: You were selecting tail.next (which is head).
            # We need the node BEFORE tail.
            new_tail = self.tail.prev 
            
            new_tail.next = self.head
            self.head.prev = new_tail
            
            self.tail = new_tail
        
        self.size -= 1
        print("-> Deleted end node")

    def delete_by_data(self, data):
        if self.head is None:
            return
        
        curr = self.head
        node_to_delete = None

        while True:
            if curr.data == data:
                node_to_delete = curr
                break
            curr = curr.next
            if curr is self.head:
                break
        
        if node_to_delete is None:
            print(f"Node {data} not found")
            return
        
        if node_to_delete is self.head:
            self.delete_at_start()
        elif node_to_delete is self.tail:
            self.delete_at_end()
        else:
            # Middle deletion
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev
            self.size -= 1
            print(f"-> Deleted {data}")

    def delete_before_node(self, target_data):
        if self.head is None or self.head == self.tail:
             print("List empty or too small")
             return

        curr = self.head
        target_node = None
        while True:
            if curr.data == target_data:
                target_node = curr
                break
            curr = curr.next
            if curr is self.head:
                break
        
        if target_node:
            node_to_delete = target_node.prev
            # Reuse logic by calling delete_by_data on the prev node's data
            # Or handle pointers manually:
            if node_to_delete is self.head:
                self.delete_at_start()
            elif node_to_delete is self.tail:
                self.delete_at_end()
            else:
                 node_to_delete.prev.next = node_to_delete.next
                 node_to_delete.next.prev = node_to_delete.prev
                 self.size -= 1
                 print(f"-> Deleted node before {target_data}")

    def delete_after_node(self, target_data):
        if self.head is None or self.head == self.tail:
             print("List empty or too small")
             return

        curr = self.head
        target_node = None
        while True:
            if curr.data == target_data:
                target_node = curr
                break
            curr = curr.next
            if curr is self.head:
                break
        
        if target_node:
            node_to_delete = target_node.next
            if node_to_delete is self.head:
                self.delete_at_start()
            elif node_to_delete is self.tail:
                self.delete_at_end()
            else:
                 node_to_delete.prev.next = node_to_delete.next
                 node_to_delete.next.prev = node_to_delete.prev
                 self.size -= 1
                 print(f"-> Deleted node after {target_data}")

# ---------------------------
# TESTING AREA
# ---------------------------
if __name__ == "__main__":
    cdll = CircularDoubly()
    
    cdll.insert_at_start(10)
    cdll.insert_at_end(20)
    cdll.insert_at_end(30)
    cdll.insert_at_start(5)
    
    cdll.traverse_forward() # Expect: 5<->10<->20<->30
    
    cdll.insert_before_node(20, 15) # Insert 15 before 20
    cdll.traverse_forward() # Expect: 5<->10<->15<->20<->30

    cdll.insert_after_node(30, 35) # Insert 35 after 30
    cdll.traverse_forward() # Expect: 5<->10<->15<->20<->30<->35
    
    cdll.delete_at_start() # Remove 5
    cdll.delete_at_end() # Remove 35
    cdll.traverse_forward() # Expect: 10<->15<->20<->30
    
    cdll.delete_by_data(15)
    cdll.traverse_forward() # Expect: 10<->20<->30
# %%

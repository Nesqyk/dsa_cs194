# Activity 1.1: The Building Block - Node
# This section defines the Node class, which is the basic building block of a singly linked list.
class Node:
    """Represents a single node in a linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

# Creation: Create four node objects
n1 = Node("Head")
n2 = Node("Middle1")
n3 = Node("Middle2")
n4 = Node("Tail")

# Activity 1.2: Manual Linking and Pointer Tracing
# Linking the nodes together in a sequence.
n1.next = n2
n2.next = n3
n3.next = n4

# Reflection Question: Why is n1.next.next proof of linking?
# This code demonstrates that nodes are linked by "next" pointers, not by contiguous memory.
# To access n3, we must start at n1, follow its "next" pointer to n2, and then follow n2's "next" pointer to n3.
# In contrast, an array would allow direct access to its elements via an index (e.g., array[2]) because they are stored contiguously in memory.
print(n1.next.next.data)

# ----

# Part 2: Traversal Logic
# Activity 2.1: Simple Standalone Traversal
# Traversal is the process of following the next pointer from the start to the end of the list.
current_node = n1
print("\n--- Simple Standalone Traversal ---")
while current_node is not None:
    print(f"Found data: {current_node.data}")
    current_node = current_node.next

# Trace the Pointer: Explanation of loop termination
# (explanatory block removed)
# ----

# Part 3: Encapsulation
# This section introduces a LinkedList class to manage the nodes using a `self.head` attribute.
class LinkedList:
    def __init__(self):
        self.head = None

    # Activity 3.1: Refactor Traversal
    # This `display` method encapsulates the traversal logic within the class.
    def display(self):
        current_node = self.head
        output = []
        while current_node is not None:
            output.append(str(current_node.data))
            current_node = current_node.next
        print(f"List: {' -> '.join(output)} -> None")

    def insert_at_start(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        print(f"-> added '{new_data}' at the beginning of the list")

    def insert_at_end(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            print(f" -> Added {new_data} to empty list (becomes new head)")
            return
        
        last_node = self.head
        
        while last_node.next:
            last_node = last_node.next
        
        last_node.next = new_node
        print(f" -> added {new_data} at the end of the list")
    
    def insert_after_node(self, prev_node_data, new_data):
        prev_node = self.head
        while prev_node is not None and prev_node.data != prev_node_data:
            prev_node = prev_node.next 
        
        if prev_node is None:
            print(f"Error: Node with data '{prev_node_data}' not found")
            return
        
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        print(f" -> Added '{new_data}' after '{prev_node.data}'")
    
    # Activity 1.1: Deletion: The Head (delete_at_start)
    def delete_at_start(self):
        if self.head is None:
            print(f"Error: Cannot delete from an empty list") 
            return
        
        current = self.head
        self.head = self.head.next
        current.next = None 
        print(f" -> Deleted head: '{current.data}'")

    # Activity 1.2: Deletion: By Value (delete_by_value)
    def delete_by_value(self, value):
        current = self.head

        if current and current.data == value:
            self.head = current.next
            current.next = None
            print(f" -> Deleted '{value}' in the list (was the head)")
            return

        prev = None
        while current and current.data != value:
            prev = current
            current = current.next

        if current is None:
            print(f"Error: Node with data '{value}' not found")
            return

        prev.next = current.next

        current.next = None
        print(f" -> Deleted {value} in the list")

    # Activity 2.1: Implementing Search (search)
    def search(self, key):
        current = self.head
        while current: 
            if current.data == key:
                print(f" -> Search: Found '{key}'")
                return True
            current = current.next
        print(f" -> Search: Key '{key}' not found")
        return False
    
    # Activity 2.2: Implementing Access by Index (access)
    def access(self, index):
        current = self.head
        count = 0

        while current is not None:
            if count == index:
                print(f" -> Accessing index {index}: Found '{current.data}'")
                return current.data
            current = current.next
            count += 1

        print(f" -> Accessing Index {index}: Error - index out of bounds")
        return None

if __name__ == "__main__":
    print("\n" + "="*50)
    print("ACTIVITY 1.1: Deletion: The Head (delete_at_start) TESTS")
    print("="*50)
    
    test_list_1 = LinkedList()
    test_list_1.insert_at_start("C")
    test_list_1.insert_at_start("B")
    test_list_1.insert_at_start("A")
    test_list_1.display()
    
    # 1. Testing the O(1) Rule: Deleting the head from a list with multiple nodes.
    print("\nTest 1: Deleting head from a multiple-node list (A, B, C)")
    test_list_1.delete_at_start() # Deletes A
    test_list_1.display() # Should be B -> C
    
    # 1. Testing the O(1) Rule: Deleting the head from a list with one node (making the list empty).
    print("\nTest 2: Deleting head from a one-node list (B -> C -> None -> Deletes B, then C)")
    test_list_1.delete_at_start() # Deletes B
    test_list_1.delete_at_start() # Deletes C (list becomes empty)
    test_list_1.display() # Should be empty
    
    # 1. Testing the O(1) Rule: Attempting to delete from an empty list (confirming the error message).
    print("\nTest 3: Attempting to delete from an empty list")
    test_list_1.delete_at_start() # Should show error

    # ---
    
    print("\n" + "="*50)
    print("ACTIVITY 1.2: Deletion: By Value (delete_by_value) TESTS")
    print("="*50)
    
    # 2. Testing: Create a list: 10 -> 20 -> 30 -> 40 -> None
    test_list_2 = LinkedList()
    test_list_2.insert_at_end(10)
    test_list_2.insert_at_end(20)
    test_list_2.insert_at_end(30)
    test_list_2.insert_at_end(40)
    print("\nInitial List for delete_by_value tests:")
    test_list_2.display()
    
    # Test 1 (Middle): Call my_list.delete_by_value(30). Display the list.
    print("\nTest 1: Deleting a middle node (30)")
    test_list_2.delete_by_value(30)
    test_list_2.display() # Should be 10 -> 20 -> 40
    
    # Test 2 (End): Call my_list.delete_by_value(40). Display the list.
    print("\nTest 2: Deleting the end node (40)")
    test_list_2.delete_by_value(40)
    test_list_2.display() # Should be 10 -> 20
    
    # Test: Deleting the Head
    print("\nTest: Deleting the head node (10)")
    test_list_2.delete_by_value(10)
    test_list_2.display() # Should be 20
    
    # Test 3 (Error): Attempt to delete a value not present in the list.
    print("\nTest 3: Attempting to delete an absent value (99)")
    test_list_2.delete_by_value(99) # Should show error

    # ---

    print("\n" + "="*50)
    print("ACTIVITY 2.1 & 2.2: Search and Access Tests")
    print("="*50)

    test_list_3 = LinkedList()
    test_list_3.insert_at_end("Zero") # Index 0
    test_list_3.insert_at_end("One")  # Index 1
    test_list_3.insert_at_end("Two")  # Index 2
    print("\nInitial List for search/access tests:")
    test_list_3.display()
    
    # 3. Testing Search: Searching for a present key (returns True)
    print("\nTest 1: Searching for 'One'")
    print(f"Result: {test_list_3.search('One')}")
    
    # 3. Testing Search: Searching for an absent key (returns False)
    print("\nTest 2: Searching for 'Three'")
    print(f"Result: {test_list_3.search('Three')}")

    # 6. Testing Access: Test accessing valid indices (e.g. 0, 1, 2)
    print("\nTest 3: Accessing valid indices")
    test_list_3.access(0) # 'Zero'
    test_list_3.access(2) # 'Two'
    
    # 6. Testing Access: Test accessing an out-of-bounds index (e.g. 10), confirming the error handling.
    print("\nTest 4: Accessing out-of-bounds index (10)")
    test_list_3.access(10) # Should show error
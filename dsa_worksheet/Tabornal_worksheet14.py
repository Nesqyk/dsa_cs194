class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        # Initialize attributes as per Activity 1.1 
        self.head = None
        self.tail = None
        self.count = 0
        self.current_state = None

    def show_state(self):
        # Traversal Helper 
        if self.current_state is None:
            print(" -> Current State: Document Empty.")
            return
        print(f" -->> Current State: '{self.current_state.data}'")

    def new_action(self, new_state):
        # Activity 2.1 & 2.2
        new_node = Node(new_state)

        # 1. Handle Empty List (Edge Case) 
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.current_state = new_node
            self.count = 1
            return

        # 2. History Truncation (Activity 2.2) 
        # Runs if we are not at the tail (meaning we undid previously)
        while self.current_state != self.tail:
            self.tail = self.tail.prev      # Move tail back 
            self.tail.next = None           # Disconnect old tail
            self.count -= 1                 # Decrement count 

        # 3. Standard Insertion (Activity 2.1) 
        # Because we truncated above, we are guaranteed to be at the end of the list.
        new_node.prev = self.current_state  # Link back to current 
        self.current_state.next = new_node  # Link current forward 
        
        self.current_state = new_node       # Move pointer to new node 
        self.tail = new_node                # Update tail to new node 
        self.count += 1                     # Increment count 

    def undo(self):
        # Activity 3.1: Conditional Traversal 
        
        # 1. Guard Clause 
        if self.current_state is None or self.current_state.prev is None:
            print("Cannot Undo: You are at the start (Head) or the list is empty.")
        else:
            # 2. CRITICAL: Use else block for movement 
            self.current_state = self.current_state.prev

    def redo(self):
        # Activity 3.2: Conditional Traversal

        # 1. Guard Clause
        if self.current_state is None or self.current_state.next is None:
            print("Cannot Redo: You are at the end (Tail) or the list is empty.")
        else:
            # 2. CRITICAL: Use else block for movement
            self.current_state = self.current_state.next


print("\n--- TEST BLOCK 1: Boundary Test (Activity 4.1) ---")

# 1. Create history: S1 <-> S2 <-> S3 
history = DoublyLinkedList()
history.new_action('S1')
history.new_action('S2')
history.new_action('S3')
print("Setup Complete: S1 <-> S2 <-> S3 created.")
history.show_state() # Expected: 'S3'

# 2. Call undo(), undo(). (Current State should be S1) 
print("\n>> Moving back to Head (S1)...")
history.undo() # Moves to S2
history.undo() # Moves to S1
history.show_state() # Expected: 'S1'

# 3. Call undo(). (Must FAIL gracefully: S1 is the Head) 
print("\n>> Testing Head Guard (Should Fail)...")
history.undo() # Should print "Cannot Undo..." message
history.show_state() # Expected: Still 'S1'

# 4. Call redo(), redo(). (Current State should be S3) 
print("\n>> Moving forward to Tail (S3)...")
history.redo() # Moves to S2
history.redo() # Moves to S3
history.show_state() # Expected: 'S3'

# 5. Call redo(). (Must FAIL gracefully: S3 is the Tail)
print("\n>> Testing Tail Guard (Should Fail)...")
history.redo() # Should print "Cannot Redo..." message
history.show_state() # Expected: Still 'S3'


# --- TEST BLOCK: Truncation Test (Activity 4.2) ---
print("\n--- STARTING TRUNCATION TEST ---")

list = DoublyLinkedList()

# Steps 1-3: Create History
list.new_action('Initial')
list.show_state()   # Expected: 'Initial' 

list.new_action('Word')
list.show_state()   # Expected: 'Word' 

list.new_action('Image')
list.show_state()   # Expected: 'Image' 

# Step 4: Undo
print("\nPerforming Undo...")
list.undo()
list.show_state()   # Expected: 'Word' 

# Step 5: New Action (Triggers Truncation)
print("\nPerforming New Action (Truncating 'Image')...")
list.new_action('New_Path')
list.show_state()   # Expected: 'New_Path' 

# Step 6: Redo (Should Fail)
print("\nAttempting Redo (Should Fail)...")
list.redo()         # Expected: "Cannot Redo..." message
list.show_state()   # Expected: 'New_Path'
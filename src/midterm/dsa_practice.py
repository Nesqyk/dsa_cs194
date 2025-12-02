class Node:

    def __self__(self, data):
        self.data = data
        self.next = None

class Linkedlist:

    def __init__(self):
        self.head =None
    
    def print_list(self):
        current = self.head
        nodes = []
        while current:
            nodes.append(str(current.data))
            current = current.next
        print(" -> ".join(nodes))

    """
    Comment: This operation is O(1) because it performs a fixed number of steps
    regardless of the list's size. It creates a new node, points it to the
    current head, and updates the head. No traversal is needed.
    """
    def insert_at_start(self ,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    """
    Comment: This operation is O(n) because we must traverse the entire list
    to find the last node. The time it takes is directly proportional to
    the number of nodes (n) in the list.
    """
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

# -- Testing Function A --
print("--- Function A: insert_at_start() O(1) Test ---")
start = Linkedlist()
for i in range(10):
    start.insert_at_start(i)
start.print_list()
print("---")

# -- Testing Function B --
end = Linkedlist()
for i in range(10):
    end.insert_at_end(i)
end.print_list()
print("---")

#---
#---

my_list = [10, 20, 30]
print(f"Original list: {my_list}")

my_list.append(40)
print(f"After append(40): {my_list}")

my_list.pop(0)

print(f"After pop(0): {my_list}")

# Comment: Include a detailed comment explaining what the computer must
#    do in memory to execute pop(0) that makes it O(n).
#
#    Executing my_list.pop(0) is an O(n) operation because Python lists are
#    implemented as dynamic arrays, which store data in a contiguous block of memory.
#    When the element at index 0 is removed, a gap is created at the beginning.
#    To fill this gap and keep the memory contiguous, the computer must **shift every
#    remaining element** one position to the left.
#
#    - The element at index 1 moves to index 0.
#    - The element at index 2 moves to index 1.
#    - ...and so on for all 'n-1' remaining elements.
#
#    This shifting process requires work proportional to the number of elements
#    in the list, resulting in a linear time complexity of O(n).
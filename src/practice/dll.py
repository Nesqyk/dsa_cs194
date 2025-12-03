class Node:

    def __init__(self, data=None, prev=None, next=None):
        self.data=data
        self.prev=prev
        self.next=next

class CircularDoubly:

    # insert_at_start
    # insert_at_end
    # insert_before_node
    # insert_after_node

    # traverse_forward
    # tarvese_backward

    # delete_at_start
    # delete_at_end
    # delete_by_data 
    # delete_before_node
    # delete_after_node

    def insert_at_start(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node

            new_node.prev = self.tail
            self.tail.next = new_node

            self.head = new_node
        self.size += 1

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node

            new_node.next = self.head
            self.head.prev = new_node

            self.tail = new_node
        self.size += 1

    def insert_before_node(self, target_data, data):
        if self.head is None:
            return
        curr = self.head
        target_node = None

        while True:
            if curr.data == target_data:
                target_node = curr
                break
            curr = curr.next

            if curr == self.head:
                break

        if target_node is None:
            return

        if target_node == self.head:
            self.insert_at_start(data)
            return

        new_node = Node(data)

        new_node.prev = target_node.prev
        new_node.next = target_node

        target_node.prev.next = new_node
        target_node.prev = new_node

    def delete_at_start(self):
        if self.head is None:
            return

        if self.head is self.tail:
            self.head == None
            self.tail == None
        else:
            new_head = self.head.next

            self.tail.next = new_head
            new_head.prev = self.tail

            self.head = new_head

    
    def delete_at_end(self):
        if self.head is None:
            return

        if self.head is self.tail:
            self.head == None
            self.tail == None
        else:
            new_tail = self.head.prev

            new_tail.next = self.head
            self.head.prev = new_tail

            self.tail = new_tail 
         
    def delete_by_data():
        # .prev.next = target_node.next
        # .next.prev = target_node.prev
        return "Hello"
                


        
        

    
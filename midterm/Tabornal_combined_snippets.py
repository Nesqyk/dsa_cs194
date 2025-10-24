# %%

class User:
    def __init__(self, name, user_id):
        self.name = name
        self._user_id = user_id
        
    # --- Q1 ---
    # What does the 'self' parameter refer to when display_info() is called
    # ANSWER: 'self' refers to the specific instance (object) of the class 
    #         on which the method is called.
    #         e.g., When 'u1.display_info()' is run, 'self' is the 'u1' object.
    def display_info(self):
        print(f"User: {self.name} (ID: {self._user_id})")

class Admin(User):
    def __init__(self, name, user_id, clearance_level):
        # --- Q2 ---
        # What is the primary purpose of the 'super().__init__(...)' call here?
        # ANSWER: Its primary purpose is to **call the constructor of the parent class (User)** #         to correctly initialize the attributes inherited from 'User' (name and user_id).
        super().__init__(name, user_id) 
        self.clearance = clearance_level
    
    def display_info(self):
        print(f"ADMIN: {self.name} | Level {self.clearance}")

def process_data(data_list):
    id_map = {}
    valid_count = 0
    
    for item in data_list:
        # --- Q3 ---
        # For the item '', which Python concept causes the 'if' statement 
        # below to be TRUE, leading to 'continue'?
        # ANSWER: The concept is **String Length** (or sequence length). 
        #         The empty string "" has a length of 0, making the condition true.
        if len(item) == 0:
            continue
        
        # This splits the string by ':' and removes whitespace from the parts
        parts = [p.strip() for p in item.split(':')] 
        
        # Checks if we have exactly 2 parts AND the second part (ID) is a number
        if len(parts) == 2 and parts[1].isdigit():
            # --- Q4 ---
            # What is the final value of 'user_name' for the input 
            # "john doe:100" after this line executes?
            # ANSWER: JOHN DOE
            user_name = parts[0].upper()
            user_id = int(parts[1])
            
            # Only process users with an even ID
            if user_id % 2 == 0:
                # --- Q5 ---
                # Based on the input 'raw_data', which two key-value pairs 
                # are added to 'id_map' by the end of this function?
                # ANSWER: {100: 'JOHN DOE'} and {204: 'ADMIN_X'}
                id_map[user_id] = user_name
                valid_count += 1
    
    return id_map, valid_count

if __name__ == "__main__":
    # --- Part 1: OOP Demonstration ---
    u1 = User("alice", 101)
    a1 = Admin("bob", 202, 5)

    print("--- 1. OOP Trace ---")
    u1.display_info() # Output: User: alice (ID: 101)
    a1.display_info() # Output: ADMIN: bob | Level 5
    
    # --- Part 2: Data Processing Demonstration ---
    raw_data = [
        "john doe:100",        # ID 100 is EVEN. Added: {100: 'JOHN DOE'}
        "jane smith:103",      # ID 103 is ODD. Skipped.
        "  admin_x : 204  ",   # ID 204 is EVEN. Added: {204: 'ADMIN_X'}
        "error_entry",         # Fails 'len(parts) == 2'. Skipped.
        ""                     # Fails 'len(item) == 0'. Skipped by 'continue'.
    ]
    
    processed_map, count = process_data(raw_data)

    print("\n--- 2. Data Process Trace ---")
    print(f"Valid Records Count: {count}") 
    print(f"Final ID Map: {processed_map}") 
# %%
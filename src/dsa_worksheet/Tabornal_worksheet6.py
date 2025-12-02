# %%

from collections import namedtuple, deque, Counter, UserString

# Problem 1: Namedtuple Library System
# A program that prints out the title of the book with most copies.

Book = namedtuple('Book', ['title','author','copies']) # Create a Book namedtuple.

# Create instances of the Book namedtuple.
harry_potter = Book('Harry Potter', 'J.K Rowling', 1000)
hunger_games = Book('Hunger Games', 'Suzanne Collins', 2123)
game_of_thrones = Book('A song of fire and Ice', 'George R. R. Martin', 600)

books = [harry_potter, hunger_games, game_of_thrones]

# Initialize variables to track the book with the most copies.
largest_copies = books[0].copies
largest_title = books[0].title

# Loop through books to find the one with the most copies.
for element in books:
    # Check if the current book has more copies than the largest found so far.
    if(largest_copies < element.copies):
        # Update the largest title and copies.
        largest_title = element.title
        largest_copies = element.copies
    
print(f"Book with most copies: {largest_title}")

# ---

# Problem 2: Deque Queue Simulation

queues = deque(["Alice","Bob", "Charlie"]) # Create a deque for a queue.
print(queues)

queues.append("Diana") # Add an element to the right end (enqueue).
print(queues)

queues.popleft() # Remove an element from the left end (dequeue).
print(queues)

# Problem 3: OrderedDict word Counter

sentence = "data structures and data algorithms".split() # Split the string into a list of words.

print(Counter(sentence)) # Count the occurrences of each word.

# Problem 4: UserString Extension - Palindrome Check

class MyString(UserString):

    # Use the Two-Pointer Technique for efficient palindrome checking.
    def is_palindrome(string: str) -> bool:
        left_pointer = 0
        right_pointer = len(string) - 1

        # Compare characters from both ends moving inward.
        while(left_pointer < right_pointer):
            if(string[left_pointer] != string[right_pointer]):
                return False
            left_pointer += 1
            right_pointer -= 1
        return True

while True:
    word = (input("Enter a word (or 0 to exit): "))

    if(word == "0"): break # Exit the loop if the user enters "0".
    # Check if the entered word is a palindrome.
    print(f"Word: {word}, Output: {MyString.is_palindrome(word)}")

# %%
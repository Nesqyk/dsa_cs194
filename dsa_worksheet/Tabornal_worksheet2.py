# Problem 1: Grading System

# Ask the user to enter integer from 0-100
grade = int(input("Please enter your grade: (0-100)"))

# Initilize the message specifically for <= 75
message = "You failed. Please review the material"

# Chaining condition and updating the value of the 'message' base on their ranges
if 80 <= grade <= 89:
    message = "Good job! You Passed with flying colors."
elif 75 <= grade <= 79:
    message = "You passed, but there's room for improvement."
elif grade >= 90:
    message = "Excellent! You are a top student."

# Print the message
print(message)

# --- 

# Problem 2: Simple Login Check

# Initialize the correct credentials
correct_user = "admin"
correct_pass = "secret123"

# Ask the user for the initial credentials
input_user = input("Please eneter your username: ")
input_password = input("Please Enter your password: ")

# Using the 'ternary operator' update value of 'message' whether the inputs were correct or not.
message = "Login Successful." if input_user == correct_user and input_password == correct_pass else "Invalid username or password."
print(message)

# ---

# Problem 3: Guess the Number

# Loop that will run forever not until the user guesses the correct number '7'.
while(True):

    # Ask for initial guess
    guess_input = int(input("Please guess a number: "))

    # Checks whether if its == 7 then prints out the message for guessing it right.
    if guess_input == 7:
        message = "Correct! You win!"
        print(message)
        break
     
    # Updates and prints out the try again; and will continue to ask
    message = "Try Again!"
    print(message)

# ---

# Problem 4: Calculating the Total and Average Score

# Initialize the 'total_score' and dummy list 'scores' with specified values.
scores = [18, 20, 19, 21,23, 20]
total_score = 0

# Get each and every score from list 'scores'
for s in scores:
    # Summation of list 'scores'; storing the sum to 'total_score'
    total_score += s

# Calculates average dynamically base on the 'total_scores' and length of the list 'scores'
average_score = total_score / len(scores)

# Prints out the output.
print(f"Total Score: {total_score}\nAverage Score: {average_score}")
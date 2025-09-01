
import string

# Problem 1: Hello, Your Name

# Prompts user to input their name
name = input("What is your name?")
# Inputs output calling 'name' somewhere.
print(f"Hello, {name}! Welcome to our DSA class")

# ---

# Problem 2: A Simple Calculator

# Prompt the user to enter two numbers
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# First, attempt to add the two variables directly.
# This line of code would produce a TypeError because the input()
# function returns strings, and you can't add two strings as numbers.
# print("The sum is: " + num1 + num2)

# Corrected version using type conversion to int()
sum_of_numbers = int(num1) + int(num2)

# Print the sum in a descriptive sentence
print(f"The sum of {num1} and {num2} is {sum_of_numbers}.")

# ---

# Problem 3: Student Information

# Intiialize dummy student information.
student_id = 1360446
student_name = "Tyrone Tabornal"
student_gpa = 1.6
is_enrolled = True

# Print the Student Information with their respective data type for each variable called.
print(f"Student ID: {student_id}, Type:  {type(student_id)}")
print(f"Name: {student_name}, {type(student_name)}")
print(f"GPA: {student_gpa}, {type(student_gpa)}")
print(f"Is enrolled: {is_enrolled}, {type(is_enrolled)}")

# ---

# Problem 4: String Manipulation

# Initialize full name with dummy data
full_name ="dela cruz, juan"

# Turns 'full_name' to uppercase
uppercase_name = full_name.upper()

# Turns 'full_name' to lowercase
titlecase_name = full_name.lower()

# Flips the uppercase_name through slicing
flipped_name = uppercase_name[11:15] + " " + uppercase_name[0:-6]

# Prints out full_name base on their attributes.
print(f"{uppercase_name}\n{titlecase_name}\n{flipped_name}")

# ---
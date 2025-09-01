# Problem 1: Flexible Greeting Function

def greet(name, department="IT Department"):
    """
    Greets a person by their name and department. The department
    is an optional parameter with a default value of "IT Department".
    
    Args:
        name (str): The name of the person.
        department (str, optional): The person's department.
                                     Defaults to "IT Department".
    """
    print(f"Hello, {name} from the {department}")

# This line calls the greet function with a new department, overriding the default.
greet("Juan Dela Cruz", "Computer Engineering")

# Note: The original code printed the return value of the function, which is None.
# To avoid this, you should call the function directly without wrapping it in a print statement
# unless the function is designed to return a string.

# Problem 2: Finding the Maximum Value

def find_max(*numbers):
    """
    Finds the maximum value from a variable number of arguments.
    
    Args:
        *numbers: A tuple containing the numbers to be evaluated.
    
    Returns:
        int or float: The maximum value found.
    """
    # Check if any numbers were provided.
    if not numbers:
        return None  # Return None or raise an error for empty input.
    
    # Initialize max_value with the first element to handle negative numbers correctly.
    max_value = numbers[0]
    
    # Iterate through the remaining numbers to find the true maximum.
    for number in numbers[1:]:
        if number > max_value:
            max_value = number
            
    return max_value

print(find_max(10, 5, 20, 15))

# Problem 3: Student Enrollment System

# Create an empty list to store the names of enrolled students.
enrolled_student = []

# Start an infinite loop to continuously prompt for student names.
while True:
    # Get student name input from the user.
    student_name = input("Enter student name (or 'done' to finish): ")
    
    # Check if the user wants to exit the loop.
    if student_name.lower() in ["done", "finish"]:
        break
    
    # Add the entered student name to the list.
    enrolled_student.append(student_name)

# After the loop, print the total count of enrolled students.
print(f"\nTotal Number of Students: {len(enrolled_student)}")
print("List of Students:")

# Iterate through the list and print each student's name.
for student in enrolled_student:
    print(student)
    
# Problem 4: List Operations

# Initialize a list of numbers.
data = [10, 20, 30, 40, 50, 60]
print(f"Original list: {data}")

# Use pop() to remove an element by its index.
# Here, we remove the element at index 0 (which is 10).
data.pop(0)
print(f"After pop(0): {data}")

# Use remove() to remove the first occurrence of a specific value.
# This removes the value 40.
data.remove(40)
print(f"After remove(40): {data}")

# Use append() to add a new element to the end of the list.
# This adds 70.
data.append(70)
print(f"After append(70): {data}")
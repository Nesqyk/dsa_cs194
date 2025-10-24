# %%

# Problem 1: Numeric and Boolean Challenge

# Get integer input from the user.
number_input = int(input("Enter a number : "))

# Check if the number is zero.
if number_input == 0:
    print("Output: Zero")
# Check if the number is positive.
elif number_input > 0:
    # Use a ternary operator to check if positive number is even or odd.
    print(f"Output: Positive {'Even' if number_input % 2 == 0 else 'Odd'}")
# If not zero or positive, it must be negative.
else:
    print("Output: Negative ")

# Problem 2: String Repetition Pattern

word_input = input("Enter a word :")
word_n = int(input("Enter n:"))
# Use the string multiplication operator to repeat the word.
print(word_input * word_n)

# Problem 3: Range & List Generation

# Generate a sequence of odd numbers.
even_numbers = list(range(1, 50, 2))
total_sum = 0
print(even_numbers)
# Iterate through the range to calculate the sum.
for e in even_numbers:
    total_sum += e
print(f"Sum : {total_sum}")

# Problem 4: Set Operations
english = {'data', 'structure', 'python', 'loop'}
math = {'set', 'function', 'data', 'graph'}

# Find common elements between the sets.
print(f"Intersection: {english & math}")
# Find elements in 'english' but not in 'math'.
print(f"Difference: {english - math}")
# Combine all unique elements from both sets.
print(f"Union: {english | math}")

# %%
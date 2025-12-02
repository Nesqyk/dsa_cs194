# Helper Functions for Data Analysis (Modified to use loops)

def find_min_max_with_loops(labels, values):
    """Finds the label and value corresponding to the min and max using loops."""
    if not values:
        return ("N/A", 0), ("N/A", 0)

    # Initialize min and max trackers
    min_value = values[0]
    min_label = labels[0]
    max_value = values[0]
    max_label = labels[0]
    
    # Use a loop to find min and max values
    for i in range(1, len(values)):
        current_value = values[i]
        current_label = labels[i]
        
        # Check for minimum
        if current_value < min_value:
            min_value = current_value
            min_label = current_label
            
        # Check for maximum
        if current_value > max_value:
            max_value = current_value
            max_label = current_label
            
    return (min_label, min_value), (max_label, max_value)

def calculate_average(values):
    """Calculates the average of a list of numbers."""
    if not values:
        return 0
    total = 0
    count = 0
    for val in values:
        total += val
        count += 1
    return total / count

# ----------------------------------------------------------------------
# Problem 1: Daily Temperatures Tracker ☀️
# ----------------------------------------------------------------------

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temperatures = [30, 32, 31, 29, 33, 34, 28]

print("--- Problem 1: Daily Temperatures Tracker Analysis ---")

# Find the hottest and coldest day using loops
(coldest_day, coldest_temp), (hottest_day, hottest_temp) = find_min_max_with_loops(days, temperatures)

# Calculate average temperature
average_temp = calculate_average(temperatures)

print(f"1. Coldest Day: **{coldest_day}** with a temperature of **{coldest_temp}°C**")
print(f"2. Hottest Day: **{hottest_day}** with a temperature of **{hottest_temp}°C**")
print(f"3. Average Temperature: **{average_temp:.2f}°C**")

# ----------------------------------------------------------------------
# Problem 2: Student Quiz Scores 💯
# ----------------------------------------------------------------------

quizzes = ["Quiz 1", "Quiz 2", "Quiz 3", "Quiz 4", "Quiz 5"]
scores = [8, 10, 9, 7, 6]
PERFECT_SCORE = 10

print("\n--- Problem 2: Student Quiz Scores Analysis ---")

# Find the highest score and corresponding quiz using loops
# We only care about the max in this case
(_, _), (highest_quiz, highest_score) = find_min_max_with_loops(quizzes, scores)

# Check for perfect score using a loop
found_perfect_score = False
for score in scores:
    if score == PERFECT_SCORE:
        found_perfect_score = True
        break # Exit loop early if found

if found_perfect_score:
    print(f"1. The Student **scored a perfect {PERFECT_SCORE}**! 🎉")
else:
    print("1. The Student did not score a perfect score.")

print(f"2. Highest Score: **{highest_score}** on **{highest_quiz}**")

# ----------------------------------------------------------------------
# Problem 3: Monthly Expenses 💸
# ----------------------------------------------------------------------

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
expenses = [2200, 2350, 2600, 2130, 2190, 1980]
TARGET_EXPENSE = 2000

print("\n--- Problem 3: Monthly Expenses Analysis ---")

# Calculate first quarter total (Jan, Feb, Mar are indices 0, 1, 2)
first_quarter_total = 0
# Use loop for summation
for expense in expenses[0:3]:
    first_quarter_total += expense

print(f"1. First Quarter Total (Jan-Mar): **${first_quarter_total}**")

# Check if 2000 was an expense using a loop
found_target_expense = False
for expense in expenses:
    if expense == TARGET_EXPENSE:
        found_target_expense = True
        break

if found_target_expense:
    print(f"2. Yes, an expense of ${TARGET_EXPENSE} was recorded.")
else:
    print(f"2. No expense of exactly ${TARGET_EXPENSE} was recorded.")

# ----------------------------------------------------------------------
# Problem 4: Book Pages Tracker 📚
# ----------------------------------------------------------------------

days_p4 = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
pages = [30, 45, 50, 20, 40, 60, 25]
TARGET_PAGES = 50

print("\n--- Problem 4: Book Pages Tracker Analysis ---")

# Calculate total pages read using a loop
total_pages_read = 0
for p in pages:
    total_pages_read += p
print(f"1. Total pages read over the week: **{total_pages_read}** pages")

# Check for 50 pages read and find the day using a loop
day_with_50 = None
for i in range(len(pages)):
    if pages[i] == TARGET_PAGES:
        day_with_50 = days_p4[i]
        break

if day_with_50:
    print(f"2. Yes, there was a day (**{day_with_50}**) with exactly **{TARGET_PAGES}** pages read.")
else:
    print(f"2. No day had exactly {TARGET_PAGES} pages read.")

# ----------------------------------------------------------------------
# Problem 5: Fitness Steps Counter 👟
# ----------------------------------------------------------------------

days_p5 = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7",
"Day 8", "Day 9", "Day 10"]
steps = [9000, 12000, 8000, 15000, 11000, 7000, 13000, 12500, 10000, 9500]

print("\n--- Problem 5: Fitness Steps Counter Analysis ---")

# Calculate average steps
average_steps = calculate_average(steps)

# Find highest day using a loop
(_, _), (highest_day, highest_steps) = find_min_max_with_loops(days_p5, steps)

print(f"1. Average Steps: **{average_steps:.0f}** steps")
print(f"2. Highest Steps: **{highest_steps}** steps on **{highest_day}**")
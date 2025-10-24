# Helper Functions for Data Analysis

def calculate_row_sums(data_matrix):
    """Calculates the sum of each row (e.g., total per student/ward/stall)."""
    return [sum(row) for row in data_matrix]

def find_max_result(labels, results):
    """Finds the label with the maximum value in a corresponding list."""
    if not results:
        return "N/A", 0
    max_value = max(results)
    max_index = results.index(max_value)
    # Use .strip() to clean up names that might have leading/trailing spaces
    max_label = labels[max_index].strip()
    return max_label, max_value

def calculate_column_averages(data_matrix):
    """
    Calculates the average of each column (e.g., average per subject/day).
    Returns a list of averages.
    """
    if not data_matrix or not data_matrix[0]:
        return []
    
    num_rows = len(data_matrix)
    num_columns = len(data_matrix[0])
    
    # Initialize column sums to zero
    column_sums = [0] * num_columns

    # Sum the columns
    for row in data_matrix:
        for i in range(num_columns):
            column_sums[i] += row[i]

    # Calculate averages
    column_averages = [total / num_rows for total in column_sums]
    return column_averages

# ----------------------------------------------------------------------
## Problem 1: Student Gradebook 📝
# ----------------------------------------------------------------------

students = ["Anthony", " Benedict", "Colin", "Daphne", "Eloise"]
grades = [
    [85, 90, 78, 88], # Anthony
    [92, 87, 85, 91], # Benedict
    [76, 80, 72, 70], # Colin
    [89, 94, 90, 92], # Daphne
    [85, 88, 84, 86]  # Eloise
]
NUM_SUBJECTS = len(grades[0])

print("\n\n--- Problem 1: Student Gradebook Analysis ---")

# Calculate student averages
student_averages = [sum(grade) / NUM_SUBJECTS for grade in grades]

# Find student with highest average (Replaced original logic with function call)
highest_student, highest_average = find_max_result(students, student_averages)

print("\n1. Student Averages:")
for i, avg in enumerate(student_averages):
    print(f"   {students[i].strip()}'s Average is: {avg:.2f}")

print(f"\n2. Student with Highest Average: **{highest_student}** with an average of: **{highest_average:.2f}**")

# Calculate subject averages (Replaced original column calculation logic with function call)
subject_averages = calculate_column_averages(grades)
subject_labels = [f"Subject {i+1}" for i in range(len(subject_averages))] # Create labels for subjects

# Find highest subject average
highest_subject, max_subject_average = find_max_result(subject_labels, subject_averages)

print(f"\n3. Subject Averages:")
print(f"   {subject_averages}")
print(f"   The highest subject average is: **{max_subject_average:.2f}** ({highest_subject})")

# ----------------------------------------------------------------------
## Problem 2: Cafeteria Sales Tracker 💰
# ----------------------------------------------------------------------

stalls = ["Noodles Stall", "Rice Meals", "Snacks & Drinks"]
sales = [
    [1200, 1300, 1100, 1400, 1500, 1600, 1700],
    [2000, 2100, 2200, 2300, 2400, 2500, 2600],
    [800, 900, 850, 950, 1000, 1100, 1050]
]

print("\n\n--- Problem 2: Cafeteria Sales Tracker Analysis ---")

# Calculate total sales per stall (Replaced manual sum with function call)
sum_sales = calculate_row_sums(sales)

# Find stall with highest total sales (Replaced original logic with function call)
highest_sales_stall, max_sales = find_max_result(stalls, sum_sales)

print(f"1. Total Sales Per Stall: {sum_sales}")
print(f"2. Stall with Highest Total Sales: **{highest_sales_stall}** with total sales of **{max_sales}**")

# ----------------------------------------------------------------------
## Problem 3: Hospital Bed Occupancy 🏥
# ----------------------------------------------------------------------

wards = ["Ward A", "Ward B", "Ward C", "Ward D", "Ward E", "Ward F"]
occupancy = [
    [20, 18, 19, 17],
    [22, 21, 20, 23],
    [15, 16, 14, 18],
    [25, 24, 26, 25],
    [18, 17, 19, 16],
    [30, 28, 29, 31]
]

TOTAL_HOSPITAL_BEDS = 120
DAYS = 4

print("\n\n--- Problem 3: Hospital Bed Occupancy Analysis ---")

# Find ward with maximum occupancy (Replaced manual sum/max with function calls)
ward_totals = calculate_row_sums(occupancy)
ward_with_max_occupancy, max_occupancy_value = find_max_result(wards, ward_totals)

print(f"1. Ward with Maximum Total Occupancy: **{ward_with_max_occupancy}** (Total: {max_occupancy_value})")

# Compute the average occupancy per ward
print("\n2. Average Occupancy Per Ward:")
for i in range(len(wards)):
    average = ward_totals[i] / DAYS
    print(f"   {wards[i]}: {average:.2f} beds")

# Calculate the overall hospital occupancy rate
total_occupied_bed_days = sum(ward_totals)
total_available_bed_days = TOTAL_HOSPITAL_BEDS * DAYS

if total_available_bed_days > 0:
    overall_occupancy_rate = (total_occupied_bed_days / total_available_bed_days) * 100
    print(f"\n3. Overall Hospital Occupancy Rate (Assuming {TOTAL_HOSPITAL_BEDS} beds):")
    print(f"   Rate: **{overall_occupancy_rate:.2f}%**")
else:
    print("\n3. Cannot calculate overall occupancy rate: Total available bed-days is zero.")

# ----------------------------------------------------------------------
## Problem 4: Library Borrowing Records 📖
# ----------------------------------------------------------------------

students_p4 = ["Anthony", " Benedict", "Colin", "Daphne"]
borrowed_books = [
    [3, 2, 4, 1, 5],
    [1, 0, 2, 3, 2],
    [0, 0, 1, 2, 1],
    [4, 3, 5, 4, 5]
]

WEEKS = 5
NUM_STUDENTS_P4 = len(students_p4)

print("\n\n--- Problem 4: Library Borrowing Records Analysis ---")

# Find which student borrowed the most books overall (Replaced manual sum/max with function calls)
student_totals_p4 = calculate_row_sums(borrowed_books)
student_with_most_books, max_books_value = find_max_result(students_p4, student_totals_p4)

print(f"1. Student who borrowed the most books overall: **{student_with_most_books}** (Total: {max_books_value}) 📚")

# Check if any student borrowed 0 books in a week
students_with_zero_weeks = []
for i in range(NUM_STUDENTS_P4):
    if 0 in borrowed_books[i]:
        students_with_zero_weeks.append(students_p4[i].strip())

print("\n2. Students who borrowed 0 books in at least one week:")
if students_with_zero_weeks:
    print(f"   Yes: **{', '.join(students_with_zero_weeks)}**.")
else:
    print("   No student borrowed 0 books in any recorded week.")

# Compute the weekly average borrowing across all students
total_books_borrowed = sum(student_totals_p4)
total_data_points = NUM_STUDENTS_P4 * WEEKS

if total_data_points > 0:
    weekly_average = total_books_borrowed / WEEKS
    average_per_student_per_week = total_books_borrowed / total_data_points

    print(f"\n3. Average Borrowing Computations:")
    print(f"   Average total borrowing per week: **{weekly_average:.2f}** books")
    print(f"   Average per student per week: **{average_per_student_per_week:.2f}** books")
else:
    print("\n3. Cannot compute weekly average: Data is empty.")

# ----------------------------------------------------------------------
## Problem 5: Computer Lab Usage Hours 💻
# ----------------------------------------------------------------------

students_p5 = ["Anthony", "Benedict", "Colin", "Daphne", "Eloise"]
lab_hours = [
    [2, 3, 4, 2, 1],
    [1, 0, 2, 3, 2],
    [4, 4, 3, 5, 4],
    [2, 2, 1, 2, 3],
    [3, 3, 2, 4, 3]
]

DAYS = 5
NUM_STUDENTS_P5 = len(students_p5)

print("\n\n--- Problem 5: Computer Lab Usage Analysis ---")

# 1. Calculate the total lab hours for each student. (Using function)
student_totals_p5 = calculate_row_sums(lab_hours)

print("1. Total Lab Hours Per Student:")
for i, total in enumerate(student_totals_p5):
    print(f"   {students_p5[i]}: **{total}** hours")

# 2. Identify the student who spent the most hours in the lab. (Using function)
student_with_most_hours, max_hours_value = find_max_result(students_p5, student_totals_p5)

print(f"\n2. Student with the Most Lab Hours: **{student_with_most_hours}** (Total: {max_hours_value} hours)")

# 3. Find out which day had the highest total lab usage across all students.
# This uses the same logic as subject average but applied to 'lab_hours'
daily_totals = [total * NUM_STUDENTS_P5 for total in calculate_column_averages(lab_hours)] # Calculate daily sums
day_labels = [f"Day {i+1}" for i in range(DAYS)]
day_with_max_usage, max_daily_usage = find_max_result(day_labels, daily_totals)

print(f"\n3. Day with the Highest Total Lab Usage:")
print(f"   **{day_with_max_usage}** had the highest usage with a total of **{max_daily_usage:.0f}** hours.")

# 4. Compute the average daily lab usage per student.
total_lab_hours = sum(student_totals_p5)

if DAYS > 0:
    average_per_student_per_day = total_lab_hours / (DAYS * NUM_STUDENTS_P5)
    print(f"\n4. Average Daily Lab Usage per Student: **{average_per_student_per_day:.2f}** hours")
else:
    print("\n4. Cannot compute average daily lab usage: Number of days is zero.")
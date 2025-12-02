# %%

"""Instructions
The attendance for 4 students over 5 practice days is recorded below:
students = [“Arman”, “Nina”, “Stella”, “Abby”]
attendance = [
    [1, 1, 0, 1, 1],  # Arman
    [1, 0, 1, 1, 1],  # Nina
    [1, 1, 1, 0, 1],  # Stella
    [0, 1, 1, 1, 0]   # Abby
] # 1 = Present, 0 = Absent

Tasks:
Compute each student’s total attendance.
Find the student with the highest attendance.
Compute attendance totals per day (e.g., how many students were present on Monday, Tuesday, etc.).
Check if any student had perfect attendance."""

students = ["Arman", "Nina", "Stella", "Abby"]
attendance = [
    [1, 1, 0, 1, 1],  # Arman
    [1, 0, 1, 1, 1],  # Nina
    [1, 1, 1, 0, 1],  # Stella
    [0, 1, 1, 1, 0]   # Abby
] # 1 = Present, 0 = Absent


student_totals = [sum(record) for record in attendance]

for i, total in enumerate(student_totals):
    print(f"Student {students[i]}'s Total Attendance : {total} ")
    if total == 5:
        print(f"{students[i]} has perfect attendance!")

max_attendance = max(student_totals)
highest_student = students[student_totals.index(max_attendance)] 

print(f"The student with the highest attendance is {highest_student} with {max_attendance} days.")

totals_per_day = [0, 0 , 0, 0, 0]

for student_record in attendance:
    for i, present in enumerate(student_record):
        totals_per_day[i] += 1

print(f"Attendance totals per day: {totals_per_day}")
# %%

# %% 

"""
=====================================================
-----------------------------------------------------
Activity Questions: Answers should be after each question
-----------------------------------------------------
1. What is the complexity class of Bubble Sort?
A: The time complexity of a bubble sort is O(n^2) in 
the worse and average case scenario. Its space complexity is
O(1).
--
2. What happens to runtime when input size doubles?
A: When n of size doubles; The average case runtime of the 
bubble sort quadruples; for the reason its complexity is
quadractic O(n^2) i.e when n becomes 2n the runtime increases
by a factor of 2n of (2n^2) / n^2 = 4n^2 / n^2 = 4.
--
3. Why is this the average case for Bubble Sort?
A: An average case for bubble sort is a random unsorted list.
This causes the algorithm to perform a substantial number of
comparison and swaps, but not as many as the worst case. 
The average case is also O(n^2) because for every element in the
list the program would have to traverse the entire list; which
would still lead to a quadratic execution time.
=====================================================
"""

import time
import random
import matplotlib.pyplot as plt

# ------------------------------------------------------
# STEP 1: Bubble Sort Implementation
# ------------------------------------------------------

"""
Pseudocode:
    procedure bubble_sort(A)
        n = length(A)
        for i = 0 to n-1 do
            for j = 0 to n-i-2 do
                if A[j] > A[j+1] then
                    swap A[j] and A[j+1]
"""
def bubble_sort(arr) -> list[int]:
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                temp_var = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp_var 
    return arr

# ------------------------------------------------------
# STEP 2: Generate Random Data (average case)
# ------------------------------------------------------
def generate_random_case(size):
    return [random.randint(1, 10_000_000) for _ in range(size)]

# ------------------------------------------------------
# STEP 3: Run Experiment (Average Case Only)
# ------------------------------------------------------

# We'll test a single input size of 10,000
input_size = 10000 
runTime = []
print("\nRunning Bubble Sort Average Case Performance Test...\n")

data = generate_random_case(input_size)
start_time = time.time()
bubble_sort(data)
end_time = time.time()
duration = end_time - start_time
runTime.append(duration)
print(f"Average Case | n={input_size:<5} | {duration:.6f} s")

# ------------------------------------------------------
# STEP 4: Visualization
# ------------------------------------------------------
plt.plot([input_size], runTime, marker='o', color='blue', label="Average Case")
plt.xlabel("Input size (n)")
plt.ylabel("Time (s)")
plt.title("Bubble Sort Average-Case Runtime")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()

# %%
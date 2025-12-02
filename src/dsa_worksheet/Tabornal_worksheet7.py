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
A: When n of size doubles; The worstcase runtime of the 
bubble sort quadruples; for the reason its complexity is
quadractic O(n^2) i.e when n becomes 2n the runtime increases
by a factor of 2n of (2n^2) / n^2 = 4n^2 / n^2 = 4.
--
3. Why is this the worst case for Bubble Sort?
A: A sorted reverse list is the worse case for a bubble sort
because for every element is in the oposite position of 
where it needs it to be. This forces the algorithm to
do the maximum number of comparison and swaps; which leads to the 
longest execution time.
=====================================================
"""

import time
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
                temp_var = arr[j] # store muna to a temp variable kay para same value gihapon for arr[k]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp_var 
    return arr

# ------------------------------------------------------
# STEP 2: Generate Worst-Case Data (reverse sorted)
# ------------------------------------------------------
def generate_worst_case(size):
    return list(range(size, 0, -1))

# ------------------------------------------------------
# STEP 3: Run Experiment (Worst Case Only)
# ------------------------------------------------------
input_sizes = [50, 100, 150, 200, 250]
# initialize empty times list
runTime = []
print("\nRunning Bubble Sort Worst Case Performance Test...\n")

for n in input_sizes:
    data = generate_worst_case(n)
    start_time = time.time()
    bubble_sort(data)
    end_time = time.time()
    duration = end_time - start_time
    runTime.append(duration)
    print(f"Worst Case | n={n:<5} | {duration:.6f} s")

# ------------------------------------------------------
# STEP 4: Visualization
# ------------------------------------------------------
plt.plot(input_sizes, runTime, marker='o', color='red', label="Worst Case") # Add values to plot
plt.xlabel("Input size (n)")
plt.ylabel("Time (s)")
plt.title("Bubble Sort Worst-Case Runtime")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()

# %%

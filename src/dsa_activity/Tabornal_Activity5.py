# %%

"""Student A received allowance money from Monday to Sunday:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
allowance = [100, 120, 90, 150, 110, 80, 130]

Tasks:
Compute the total allowance for the week.
Find the day with the highest allowance.
Find the day with the lowest allowance.
Check if the student ever received exactly 100 pesos."""

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
allowance = [100, 120, 90, 150, 110, 80, 130]

total_allowance = sum(allowance)

highest_day = days[allowance.index(max(allowance))]
lowest_day = days[allowance.index(min(allowance))]

print(f"Highest Allowance is at {highest_day} with : {max(allowance)}")
print(f"Lowest Allowance is at {lowest_day} with : {min(allowance)}")

if 100 in allowance:
    print("Yes, the student received exactly 100 pesos.")
else:
    print("No, the student never received exactly 100 pesos.")
# %%

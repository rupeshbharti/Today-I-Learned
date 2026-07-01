# Task 4: Importing the Package using specific styles

# 1. Import discount module with an alias
import shop_package.discount as disc

# 2. Import calculate_total directly from billing module
from shop_package.billing import calculate_total

# Import apply_tax to ensure we can call every function inside the package
from shop_package.billing import apply_tax

print("--- Testing Task 4 Import Syntax ---")

# 3. Call every function inside the package

# Testing discount functions using the 'disc' alias
discount_1 = disc.apply_discount(1000, 10)
print(f"disc.apply_discount(1000, 10)  -> {discount_1}")

discount_2 = disc.flat_discount(1000)
print(f"disc.flat_discount(1000)        -> {discount_2}")

# Testing billing functions
prices_list = [100, 200, 300]
total_sum = calculate_total(prices_list)
print(f"calculate_total([100, 200, 300]) -> {total_sum}")

taxed_total = apply_tax(total_sum)
print(f"apply_tax({total_sum})               -> {taxed_total:.2f}")


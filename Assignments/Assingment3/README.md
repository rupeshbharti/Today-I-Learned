## __How to Run__

- Use __Jupyter Notebook__ or __Google Colab__ for easy outputs.
    - In each task run the cells serially one by one. 
- If Using __VS Code__, copy the code and then run it in VS code.
    - If any task contains 2 or more than 2 cells then copy all cells and combine them in to a single.
    - And then run it.

### Recommended ---> Use **Jupyter Notebook** or **Google Colab**

### Summary of Assignment 3: Functions

This notebook practices Python functions, default arguments, lambda functions, `map()`, `filter()`, and a small menu-driven mini project.

### Task 1: Apply Discount

- Created a function named `apply_discount(price, discount_percent=5)`.
- The function calculates the discounted price by subtracting the discount amount from the original price.
- It uses a default discount of 5% when no discount value is provided.
- Tested the function with both a custom discount and the default discount.

### Task 2: Factorial Function

- Created a function named `factorial(n)` to calculate the factorial of a number.
- Added validation for negative numbers and displayed an error message when the input is invalid.
- Returned `1` for factorial values of `0` and `1`.
- Used a loop to calculate factorial values for positive numbers.
- Tested the function with positive, zero, and negative inputs.

### Task 3: GST Using Lambda

- Created a lambda function named `gst`.
- The function adds 18% GST to the given price.
- Tested the lambda function with a sample price.

### Task 4: GST on Price List Using `map()`

- Created a list of prices.
- Used `map()` with a lambda function to add 18% GST to every price in the list.
- Converted the `map` object into a list before printing because `map()` returns an iterator.

### Task 5: Filtering Prices Using `filter()`

- Created a list of prices.
- Used `filter()` with a lambda function to get prices greater than 500.
- Used another `filter()` expression to get prices less than 500.
- Converted the filtered results into lists before printing.

### Task 6: Processing Prices

- Created a function named `process_price(prices)`.
- Used `map()` to apply a 10% discount to each price.
- Used `filter()` to keep only discounted prices greater than 300.
- Returned both the discounted price list and the filtered price list.

### Task 7: Mini Project - Price Management System

- Built a menu-driven price management program.
- Created `add_price()` to add a new price to the list.
- Created `get_average_price()` to calculate the average price and return `0` when the list is empty.
- Created `get_max_price()` to find the highest price and return `0` when the list is empty.
- Used a `while True` loop to repeatedly show menu options.
- Allowed the user to add prices, view the average price, view the highest price, or quit the program.
- Added input validation to handle invalid numbers and negative prices.

### Overall Learning

Through this notebook, the main concepts practiced are function creation, default parameters, return values, loops, conditional statements, lambda functions, `map()`, `filter()`, list conversion, input validation, and building a simple interactive Python program.
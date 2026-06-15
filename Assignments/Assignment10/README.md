# Assignment 10: Pandas

This assignment introduces basic Pandas operations using two small datasets: student marks and daily sales revenue. The notebook demonstrates how to create Series and DataFrames, inspect data, perform calculations, filter rows, group records, and visualize values using Pandas plotting.

## Notebook

- File: `assignment10.ipynb`
- Library used: `pandas`
- Main topic: Pandas data analysis basics

## Task Summary

### Task 1: Create and Inspect a Pandas Series

A list of student marks `[78, 85, 90, 66, 72]` is converted into a Pandas Series.

Operations performed:

- Created a Series from a Python list.
- Displayed Series values.
- Checked the index using `series.index`.
- Checked the data type using `series.dtype`.
- Displayed the first value using `head(1)`.
- Displayed the last two values using `tail(2)`.

### Task 2: Perform Arithmetic Operations on a Series

Basic arithmetic operations are applied to the marks Series.

Operations performed:

- Added `5` marks to every value.
- Subtracted `2` marks from every value.
- Multiplied every mark by `1.05`.
- Divided every mark by `2`.

This task shows how Pandas applies operations element-wise across a Series.

### Task 3: Analyze Series Statistics

The marks Series is analyzed using statistical methods.

Operations performed:

- Used `describe()` to display count, mean, standard deviation, minimum, quartiles, and maximum.
- Calculated mean marks: `78.2`.
- Found maximum marks: `90`.
- Found minimum marks: `66`.
- Calculated total marks: `391`.
- Used `apply()` with a lambda function to check which students passed with marks greater than or equal to `70`.
- Counted students who passed: `4`.

### Task 4: Create and Inspect a DataFrame

A student DataFrame is created using names, marks, and subjects.

Dataset:

| Name | Marks | Subject |
| --- | ---: | --- |
| Amit | 78 | Math |
| Neha | 85 | Math |
| Rahul | 90 | Science |
| Sneha | 66 | Science |
| Pooja | 72 | Math |

Operations performed:

- Created a DataFrame from a dictionary.
- Displayed the first three rows using `head(3)`.
- Displayed the last two rows using `tail(2)`.
- Checked the DataFrame shape: `(5, 3)`.
- Displayed column names: `Name`, `Marks`, and `Subject`.

### Task 5: Explore and Sort the DataFrame

The student DataFrame is inspected and sorted.

Operations performed:

- Used `info()` to view column data types and non-null counts.
- Used `describe()` to summarize the numeric `Marks` column.
- Displayed all rows using `head()` and `tail()`.
- Sorted students by marks in descending order.
- Reset the sorted DataFrame index using `reset_index(drop=True)`.

Sorted marks order:

| Name | Marks | Subject |
| --- | ---: | --- |
| Rahul | 90 | Science |
| Neha | 85 | Math |
| Amit | 78 | Math |
| Pooja | 72 | Math |
| Sneha | 66 | Science |

### Task 6: Filter and Group Data

Filtering and grouping operations are performed on the student DataFrame.

Filtering performed:

- Selected students with marks greater than `75`: Amit, Neha, and Rahul.
- Selected students from the Math subject: Amit, Neha, and Pooja.
- Calculated average marks: `78.2`.
- Selected students scoring above average: Neha and Rahul.
- Selected students scoring below `70`: Sneha.

Grouping performed:

- Calculated average marks by subject:

| Subject | Average Marks |
| --- | ---: |
| Math | 78.33 |
| Science | 78.00 |

- Counted students by subject:

| Subject | Count |
| --- | ---: |
| Math | 3 |
| Science | 2 |

- Found maximum marks by subject:

| Subject | Maximum Marks |
| --- | ---: |
| Math | 85 |
| Science | 90 |

### Task 8: Visualize Student Marks

Pandas plotting is used to visualize student marks.

Charts created:

- Bar chart of marks by student name.
- Line chart of marks.
- Histogram of marks distribution.

This task shows how Pandas can quickly create simple plots from DataFrame and Series data.

### Task 9: Analyze Sales Revenue

A sales DataFrame is created with daily revenue values.

Dataset:

| Day | Revenue |
| --- | ---: |
| Mon | 1200 |
| Tue | 1500 |
| Wed | 900 |
| Thu | 2000 |
| Fri | 1800 |

Operations performed:

- Calculated total revenue: `7400`.
- Calculated average daily revenue: `1480.0`.
- Found highest daily revenue: `2000`.
- Selected days with revenue below average: Monday and Wednesday.
- Created a bar chart showing revenue by day.

## Key Concepts Practiced

- Creating Pandas Series and DataFrames.
- Inspecting data using `head()`, `tail()`, `shape`, `columns`, `info()`, and `describe()`.
- Performing element-wise arithmetic on Series.
- Calculating summary statistics such as mean, max, min, and sum.
- Filtering rows using conditions.
- Using `isin()` for category-based filtering.
- Grouping data with `groupby()`.
- Sorting values and resetting indexes.
- Creating basic plots with Pandas.

## Conclusion

Assignment 10 covers the core Pandas skills needed for beginner-level data analysis. It starts with Series operations, moves into DataFrame creation and inspection, then applies filtering, grouping, sorting, and visualization to student marks and sales revenue datasets.

## __How to Run__

- Use __Jupyter Notebook__ or __Google Colab__ for easy outputs.
    - In each task run the cells serially one by one. 
- If Using __VS Code__, copy the code and then run it in VS code.
    - If any task contains 2 or more than 2 cells then copy all cells and combine them in to a single.
    - And then run it.

### Recommended ---> Use **Jupyter Notebook** or **Google Colab**
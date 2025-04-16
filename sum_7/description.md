Write a function `sum_7(list_a, list_b)` that:

Uses list comprehension to create a list of all possible tuples (a, b), where a is from list_a and b is from list_b.

From these pairs, count how many unique combinations add up to 7.
- A pair like (3, 4) and (4, 3) should be treated as the same and only counted once.
- Each input list contains only unique numbers, so you don't need to worry about duplicates in one list.

For example:
- `sum_7([0, 1, 2, 3], [4, 5, 6, 7, 8, 9])` → `4`
- `sum_7([2, 3, 8, 10], [4, 5, -1])` → `3`
- `sum_7([0, 2, 4], [6, 8])` → `0`

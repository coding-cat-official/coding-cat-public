Write a function that takes a list of integers and returns the number of **peaks** in the list. A **peak** is an element that is **greater than both its immediate neighbours**. The first and last elements of the list cannot be peaks because they only have one neighbour each. The list will contain at least three integers.

For example:
- `count_peaks([1, 3, 2, 4, 1]) → 2 (peaks at 3 and 4)`
- `count_peaks([1, 2, 3, 4, 5]) → 0`
- `count_peaks([5, 1, 5, 1, 5]) → 1`
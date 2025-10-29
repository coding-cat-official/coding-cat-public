Write a function `is_exponential(lst)` that takes in a list of integers `lst`. The function should return `True` if the elements in the list are in increasing order and each element is exactly double the previous one. If either condition is not met, return `False`.

For example:
- `is_exponential([1, 2, 4, 8])` should return `True`
- `is_exponential([1, 2, 3, 4])` should return `False` (not all elements double the previous one)
- `is_exponential([2, 4, 8, 17])` should return `False` (last element does not double the previous one)
- `is_exponential([1])` should return `True` (a single element is trivially in order)

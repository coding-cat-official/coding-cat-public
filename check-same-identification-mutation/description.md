
Write a function `check_id( l1, l2, target ) → bool` which returns True if the target can be found in both lists(arrays) at the same position. Otherwise, False.

For example:
- `check_id([2, 3, 10], [3, 10, 2], 2) → False`  
- `check_id([2, 3, 10], [2, 10, 3], 3) → False`
- `check_id([2, 3, 10], [2, 10, 3], 2) → True`  # 2 is at index 0 in both list : they have the same id.


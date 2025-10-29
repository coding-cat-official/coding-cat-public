Write a function `ordered_insert(lst, num)` that takes two arguments:
1. `lst`: A list of integers in ascending order.
2. `num`: An integer to insert into the list.

The function should return a new list with `num` inserted into the correct position so that the order is preserved. You are not allowed to use any sorting functions or libraries; the list should already be sorted, and `num` should be placed in the correct spot directly.


```python
ordered_insert([1, 3, 5, 7], 4)   # returns [1, 3, 4, 5, 7]
ordered_insert([10, 20, 30], 25)  # returns [10, 20, 25, 30]
ordered_insert([2, 4, 6], 8)      # returns [2, 4, 6, 8]
ordered_insert([], 5)             # returns [5]
```

Given an array of integers `nums` and a boolean variable `is_even`, return the largest possible sum of a subarray that satisfies the following conditions:

- If `is_even` is `True`, return the largest sum of a subarray consisting only of even integers, ensuring that no two consecutive elements are selected.
  
- If `is_even` is `False`, return the largest sum of any subarray (regardless of it is even or odd) where no two consecutive elements are selected.

****

```largest_sum([0, -2, 0, -4, 0, -6], False) -> 0```,  the greatest subsequence is ```[0,0,0]```
```largest_sum([1, 2, 3, 4, 5, 6], False) -> 12```,  the greatest subsequence is ```[2, 4, 6]```
```largest_sum([7, 2, 3, 1, 50], True) -> 12```, the greatest subsequence is ```[2, 50]```, because only even integers are considered.

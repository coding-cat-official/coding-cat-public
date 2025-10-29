Write a function `rotate_list(lst, n)` that takes in a list `lst` and an integer `n`, which represents the number of times to rotate the list clockwise. Each clockwise rotation moves the last element of the list to the front. The function should return the modified list after `n` rotations.

For example:
- `rotate_list([1, 2, 3, 4], 1)` should return `[4, 1, 2, 3]`
- `rotate_list([1, 2, 3, 4], 2)` should return `[3, 4, 1, 2]`
- `rotate_list([1, 2, 3, 4], 4)` should return `[1, 2, 3, 4]` (a full rotation brings it back to the original list)
- `rotate_list([1, 2, 3], 5)` should return `[3, 1, 2]`

*Hint*: Use slicing to split the list around the rotation point and rearrange it.

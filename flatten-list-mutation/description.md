Write a recursive function `flatten_list` that takes a nested list of arbitrary depth and returns a flattened list. The function should handle lists that contain other lists, integers, and/or other data types.

EXAMPLES:

Input: `[1, [2, 3, [4, 5]], 6]`
Output: `[1, 2, 3, 4, 5, 6]`

Input: `[1, 'a', [2, 'b', [3, 'c']]]`
Output: `[1, 'a', 2, 'b', 3, 'c']`
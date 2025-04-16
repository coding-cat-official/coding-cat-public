Given 2 strings, `list_1` and `list_2`, return the number of times they contain the same numbers in the same positions. For example, if `list_1 = [1, 3, 4, 6, 6, 8]` and `list_2 = [2, 3, 5, 3, 6, 7, 9]`, then the result would be `2`, since they share the values `3` and `6` at index `1` and `5` respectively. <em>Notes: lists do not need to be of the same length, and they can be empty</em>. <em>They can also be nested lists</em>.

- `list_match([1, 3, 4, 6, 6, 8], [2, 3, 5, 3, 6, 7, 9]) -> 2`
- `list_match([56, 78, 0, 34, 5, 7, 90], [12, 87, 0, 34, 7, 5, 90]) -> 3`
- `list_match([1, 2], [1, 4, 5, 6, 89, 1]) -> 1`

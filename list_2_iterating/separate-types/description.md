Write a function `separate_types(lst)` that takes a list `lst` containing elements that may be of type `int`, `str`, or `bool`. The function should return a list of three lists:
1. The first list should contain all the integers in `lst`.
2. The second list should contain all the booleans in `lst`.
3. The third list should contain all the strings in `lst`.

For example:
- `separate_types([1, "apple", True, 2, "banana", False])` should return `[[1, 2], [True, False], ["apple", "banana"]]`
- `separate_types(["hello", 42, False, 0, "world"])` should return `[[42, 0], [False], ["hello", "world"]]`
- `separate_types([])` should return `[[], [], []]`

*Hint*: recall you can use the `type()` function to find the type of any piece of data. `type()` will return `int`, `bool`, or `str` depending on if it's an integer, boolean value, or string

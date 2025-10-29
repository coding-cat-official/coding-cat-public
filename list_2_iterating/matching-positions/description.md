Write a function `matching_positions(lst1, lst2)` that takes in two lists of strings, `lst1` and `lst2`. The function should return the count of positions where the strings in `lst1` and `lst2` are the same. 

For example:
- `matching_positions(["hi", "bye"], ["hi", "hello"])` should return `1` (first elements match).
- `matching_positions(["apple", "banana", "cherry"], ["apple", "banana", "grape"])` should return `2` (first and second elements match).
- `matching_positions(["cat", "dog"], ["mouse", "dog"])` should return `1` (second elements match).
- `matching_positions(["a", "b", "c"], ["a", "x", "c"])` should return `2` (first and third elements match).

*Note*: The lists will always be of the same length.

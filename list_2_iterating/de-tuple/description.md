Write a function `transform_data(data: List[Tuple[str, int]]) -> List[int]` that takes in a list of tuples, each containing a string and an integer. The function should return a new list containing only the integer values from each tuple.

For example:
- `de_tuple([("apple", 1), ("banana", 2), ("cherry", 3)])` should return `[1, 2, 3]`.
- `de_tuple([("x", 10), ("y", 20), ("z", 30)])` should return `[10, 20, 30]`.
- `de_tuple([])` should return `[]`.

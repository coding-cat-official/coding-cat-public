
Complete the function `def list_equate(list1: list[int], list2: list[int]) -> bool:` to check if 2 given lists of arbitrary length with random integer elements equal one another. It does not matter how many times a number is repeated, so long as it appears once the lists are equal. Each list will have at minimum 1 value.

Return `True` if the lists are equal and `False` otherwise.

For example:
- `list_equate([1, 2, 3], [2, 3, 1]) -> True`
- `list_equate([1, 1, 2, 1], [2, 1]) -> True`
- `list_equate([5, 4], [6, 4]) -> False`
- `list_equate([1, 2, 3], [1, 2, 3, 4]) -> False`
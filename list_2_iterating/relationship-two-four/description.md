
Write a function `four-two-relationship(lst :List[int]) -> bool` that determines the relationship between four and two based on the following conditions:
- Return True if 2 and 4 appear anywhere in the list, but DO NOT appear side by side. 
- If there is no 2 or 4 in the list, OR each 2 and 4 appear side-by-side, return False. 

For example:
- `four-two-relationship([1, 2, 3]) -> False`
- `four-two-relationship([8, 1, 2, 4]) → False`
- `four-two-relationship([4, 7, 1, 2, 9, 5]) → True`

Given a list of string letters `["a","b","c"]` and a list of numbers `[1,2,3,4]`, return all possible letter-number combinations. For each letter, iterate through all numbers before moving to the next letter.

For example:
- `make_combinations(["a","b","c"], [2,3])` → [['a', 2], ['a', 3], ['b', 2], ['b', 3], ['c', 2], ['c', 3]]
- `make_combinations(["a"], [1,2,3,4])` → [['a', 1], ['a', 2], ['a', 3], ['a', 4]]
- `make_combinations(["a","c"], [1,2,3,4])` → [['a', 1], ['a', 2], ['a', 3], ['a', 4], ['c', 1], ['c', 2], ['c', 3], ['c', 4]]

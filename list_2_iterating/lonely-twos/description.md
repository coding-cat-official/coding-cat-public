Write a function `lonely_twos(nums)` that takes a list of integers `nums` and returns `True` if there are more occurrences of `2` that do *not* have another `2` adjacent to them than occurrences of `2` that *do* have another `2` adjacent. Note, we count adjacent 2s _twice_, once for each 2, so the list `[2, 0, 2, 2]` has `1` single two, and `2` adjacent twos.

A `2` is considered "lonely" if it has no other `2`s immediately next to it in the list.

For example:
- `lonely_twos([1, 2, 3, 2, 2, 4, 2])` should return `False` because there are two lonely `2`s (the first and last ones) and two adjacent pair of `2`s.
- `lonely_twos([2, 2, 2])` should return `False` because there are no lonely `2`s and three adjacent `2`s.
- `lonely_twos([1, 2, 3, 4])` should return `True` because there is one lonely `2` and no adjacent `2`s.

*Constraints*:
- The input list `nums` will contain at least one element.

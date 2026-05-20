Write a function `function4(num)` that takes as input an `int` and returns `True` if `num` is greater than or equal to 10, and `False` otherwise.

Now that we know about booleans, we can move on to operators that use and compare them.

There are a couple ways to compare two values:
- `==`: returns `True` if the values are equal in value and `False` otherwise.
  - `5 == 5` → `True`
  - `"word" == 'word'` → `True` (the single VS double quotes do not change the value)
  - `"word" == "Word"` → `False` (capitalization matter when using `str`!!)
  - `5 == "5"` → `False` (one is an `int`, the other a `str`)

- `!=`: returns `True` if values are **not** equal in value and `False` otherwise. The opposite of the previous operator.
  - `5 != 5` → `False`
  - `"word" != 'word'` → `False`
  - `5 != "5"` → `True`

- `>` / `<` / `>=` / `<=`: works the same as it does in math. Returns `True` if the equality is true, and `False` otherwise.
  - `5 < 10` → `True`
  - `2 > 5` → `False`
  - `20 >= 20` → `True`
  - `1 > 1` → `False`

If you want to compare multiple values to each other, you're going to need to know about some comparison operators.

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

<hr/>

Write a function `ten_or_greater(num)` that takes as input an `int` and returns `True` if `num` is greater than or equal to 10, and `False` otherwise.

For example:
- `ten_or_greater(5)` → `False`
- `ten_or_greater(11)` → `True`
- `ten_or_greater(10)` → `True`

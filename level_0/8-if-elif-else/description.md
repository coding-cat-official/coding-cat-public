If you want to use conditions in your code, you're going to need the conditional statements `if`, `elif` and `else`.

`if` statements are formatted like this:
```
if condition:
    # do things if condition == True
# do this afterwards, regardless of result
```

Example:
```
note = ""
if num > 10:
    note = "number greater than 10"
return note
```

`if` statements can be paired with an `else` statement. As you might guess, the contents of `else` run when the `if` condition is `False`.

`else` statements are formatted like this:
```
note = ""
if num >= 10:
    note = "num is 10 or greater"
else:
    note = "num is less than 10"
return note
```

Finally, you can chain `if` statements together to make branching paths using `elif`. `elif` statements combine `else` and `if` to make a statement that only runs if the `if` above it was `False`.

Tip: You don't have to check if a `bool` is `==` to `True`, `bool`s can be their own condition! For example, if `x` is a `bool`, you can just write `if x:`, and it means the same as `if x == True:`

Example:
```
note = ""
if num >= 10:
    note = "num is 10 or greater"
elif num <= 5:   # only checks this if num >= 10 is False
    note = "num is 5 or less"
else:
    note = "num is between 6 and 9"
return note
```

<hr/>

Write a function `if_elif_else(bool1, bool2)` that takes two booleans as input. If `bool1` is `True` it should return `1`, elif `bool2` is `True` it should return `2`, else return `0`.

Some examples:
- `if_elif_else(True, False)` → `1`
- `if_elif_else(False, True)` → `2`
- `if_elif_else(False, False)` → `0`

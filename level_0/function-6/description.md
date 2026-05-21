If you want to use conditions in your code, you're going to need the conditional statements `if`, `elif` and `else`.

`if` statements are formatted like this:
```
if condition:
    # do things
# do this afterwards, regardless of result
```

Example:
```
if num > 10:
    comment = "number greater than 10"
return comment
```

`if` statements can be paired with an `else` statement. As you might guess, the contents of `else` run when the `if` condition is `False`.

`else` statements are formatted like this:
```
if num >= 10:
    comment = "num is 10 or greater"
else:
    comment = "num is less than 10"
return comment
```

Finally, you can chain `if` statements together to make branching paths using `elif`. `elif` statements combine `else` and `if` to make a statement that only runs if the `if` above it was `False`.

Example:
```
if num >= 10:
    comment = "num is 10 or greater"
elif num <= 5:   # only checks this is num < 10
    comment = "num is 5 or less"
else:
    comment = "num is between 6 and 9"
return comment
```

<hr/>

Write a function `function6(bool1, bool2)` that takes two booleans as input. If `bool1` is `True` it should return `1`, otherwise if `bool2` is `True` it should return `2`, else return `0`.

If you want to use conditions in your code, you're going to need the conditional statements `if`, `elif` and `else`.

`if` statements are formatted like this:
```
if num > 10:
    # if num is greater than 10, do this
# do this afterwards, regardless of num
```

`if` statements can be paired with an `else` statement. As you might guess, the contents of `else` run when the `if` condition is `False`.

`else` statements are formatted like this:
```
if num >= 10:
    # if num is 10 or greater, do this
else:
    # otherwise, do this
# do this afterwards, regardless of num
```

Finally, you can chain `if` statements together to make branching paths using `elif`. `elif` statements combine `else` and `if` to make a statement that only runs if the `if` above it was `False`.

Example:
```
if num >= 10:
    # if num is 10 or greater, do this
elif num <= 5:
    # skipped if num >= 10 is True
    # if num is 5 or less, do this
else:
    # if all above was False (num is between 6 and 9), do this
# do this afterwards, regardless of num
```

<hr/>

Write a function `function6(bool1, bool2)` that takes two booleans as input, and returns `"bool1"` if `bool1` is `True`, otherwise return `"bool2"` if `bool2` is `True`, otherwise return `"nope"`. 

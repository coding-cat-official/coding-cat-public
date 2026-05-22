<strong>Parameters</strong>

Parameters are where functions get a little more dynamic. Values are passed to the function in the parentheses `()` after the name when it is called, and then they are available within the function as variables.

For example, if you defined a function called `function2` with two parameters like this:
```
def function2(num1, num2):
    # do stuff
```

If you were to run `function2(10, 25)`:
- This is calling `function2` with 10 and 25
- In this execution, `num1` = 10 and `num2` = 25

<hr/>

<strong>Return Statements</strong>

`return` statements are how you get things out of functions. Coding Cat takes the function you write and passes it a set list of inputs, and checks the expected result against what your code returns.

For example:
```
def get_difference(num1, num2):
    diff = num1 - num2
    return diff

# Running `get_difference(10, 25)` would return -15.
```

You can create your own variables like I did with `diff` here, simply give it a name and a value!

If you aren't sure how your code is running, `print` statements can help you figure that out! Just be sure to remove them later once you know everything works!

<hr/>

Write a function `sum_nums(num1, num2)` that takes in 2 numbers, `num1` and `num2` and returns their sum.

For example:
- `sum_nums(10, 25)` → `35`
- `sum_nums(1, 1)` → `2`
- `sum_nums(-5, -5)` → `-10`

Note: Try writing `print(num1)` in your `sum_nums` and see what happens!

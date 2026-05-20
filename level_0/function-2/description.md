Write a function `function2(num1, num2)` that takes in 2 numbers, `num1` and `num2` and returns their sum.

Parameters are where functions get a little more dynamic. Values are passed to the function in the parentheses after the name when it is called, and then they are available within the function as variables.

For any function you write, you can call the parameters whatever you want, `num1` and `num2` are just suggestions.

Example:

`function2(10, 25)`
* This is calling function2 with 10 and 25
* In this execution, `num1` = 10 and `num2` = 25

`return` statements are how you get things out of functions. Coding Cat takes the function you write and passes a set list of inputs, and checks the expected result against what your code returns.

For example:
```
def get_difference(num1, num2):
    diff = num1 - num2
    return diff

# Running `get_difference(10, 25)` would return -15.
```

You can create your own variables like I did with `diff` here, simply give it a name and a value!

If you aren't sure how your code is running, `print` statements can help you figure that out! Just be sure to remove them later once you know everything works!

Try writing `print(num1)` in your `function2` and see what happens!
Write a function `function3(var)` that takes as input a value (it could be anything) and returns its type.

To complete this problem, we're going to have to learn about data types.

In Python, there are many data types, but the most common ones you'll see on Coding Cat are `bool`, `int`, `float` and `str`.

- `bool`: Boolean, it can be `True` or `False`. That's it.

- `int`: Integer, positive or negative whole numbers.
- `float`: Floating Point number, a number with a decimal value. Whole number floats still have a decimal value of .0 (ex: `10.0`).

- `str`: String, a sequence of 0 or more characters (not just letters) wrapped in quotes (`''`/`""`).
  - "Eric"
  - ""
  - 'fdajfndsjl nfjnsh vgfvbgf'
  - "50" (While this looks like an `int`, the quotes mean it is a `str`)

There are quite a few more types to learn about, but to keep things simple, these are just some to start with. For more information on types, check out [this blog post]()

You can get the type of a variable by running `type()` on it. Have a look at the starter code. *Don't worry about `__name__`, it will not come up* This function will return a `str` representing the type of the variable `number`. It currently does not use `var`.

For example:
`num = 5, word = "hello", no = False`
- `type(num).__name__ → 'int'`
- `type(word).__name__ → 'str'`
- `type(no)__name__ → 'bool'`

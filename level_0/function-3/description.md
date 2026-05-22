To do more with functions, we're going to have to learn about data types.

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

You can get the type of a variable by passing it to a pre-made Python function called `type()` by putting the variable within the parentheses like so: `type(variable_name)`. `type().__name__` returns a `str` that represents the type of variable entered.

Example:
```
x = 5
y = "hello"
z = False
```

- `type(x).__name__` → `'int'`
- `type(y).__name__` → `'str'`
- `type(z).__name__` → `'bool'`

<br/>

Have a look at the starter code. When you hit run, the function will be passed different types of variables. We want it to return each variable's type. 

**It currently only returns the type of the variable `number`, we want it to use `var`. Do not change `__name__`.**

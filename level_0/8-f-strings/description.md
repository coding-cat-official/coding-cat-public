There are more ways to construct strings than using concatenation.

The simplest and most effective method for our purposes are F-strings. They allow you to put your variable names straight into a string definition and Python will insert the value for you when run!

The "F" stands for "formatted", and is also how you create an f-string. First, define a `str` as usual, then put an `f` in front of the quotes, on the outside. To insert a value, wrap the variable name in `{}`.

For example:
`x = 10, greeting = "Howdy", cost = 10.25`
- `f"x is equal to {x}."` → `"x is equal to 10."`
- `f"{greeting}!"` → `"Howdy!"`
- `f"Tickets cost ${cost}."` → `"Tickets cost $10.25."`

<hr/>

Write a function `hello_greeting(name: str)` that takes a string `name` as input and returns a greeting of the form `"Hello Name!"`, where `Name` is the input string.

For example:
- `hello_greeting("Bob")` → `"Hello Bob!"`
- `hello_greeting("Alice")` → `"Hello Alice!"`
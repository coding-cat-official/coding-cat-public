Write a function `double_nth(str: str, n: int) -> str`  that takes 2 inputs: a string `str` and an integer `n` . The function looks at the string and counts letters starting from 1 (not 0), restarting from 1 everytime `n`  is reached.  It should return a new string where every `n`-th character is repeated based on the following conditions:

- If everything is normal, return a string with every `n`-th character repeated.
- If `n` is greater than the string length, return the original string.
- If `n` is less than or equal to 0, return `""`.
- if `str` is empty, return `""`.


For example:
- `double_nth("programming", 2)` → `"prroggraammminng"`
- `double_nth("hi", 3)` → `"hi"`
- `double_nth("bonjour", -2)` → `""`
- `double_nth("null", 0)` → `""`
- `double_nth("", -2)` → `""`


Write a function `double_n-th(str: str, n: int) -> str`  that takes 2 inputs: a string `str` and an integer `n` . The function looks at the string and counts letters starting from 1 (not 0), restarting from 1 everytime `n`  is reached.  It should return a new string where every `n`-th character is repeated based on the following conditions:

- If everything is normal, return a string with every `n`-th character repeated.
- If `n` is greater than the string length, return the original string.
- If `n` is less than or equal to 0, return `""`.
- if `str` is empty, return `""`.


For example:
- `double_n-th("programming", 2)` → `"prroggraammminng"`
- `double_n-th("hi", 3)` → `"hi"`
- `double_n-th("bonjour", -2)` → `""`
- `double_n-th("null", 0)` → `""`
- `double_n-th("", -2)` → `""`


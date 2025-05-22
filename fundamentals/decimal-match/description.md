Write a function `decimal_match(n: int, f: float) -> bool` that takes two inputs: an integer `n` and a floating-point number `f`. The function should return `True` if the decimal part of `f` contains the integer `n` in sequence; otherwise, it should return `False`. 

For example:
- `decimal_match(11, 0.11) → True` because `11` appears in the decimal part of `0.11`. 


**Note:** The integer part will always be two digits long, and the decimal part will have exactly two digits. For example: 11 and 0.11 are valid, but 111 or 0.111 (or longer) are not.

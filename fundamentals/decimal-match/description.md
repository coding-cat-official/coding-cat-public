Write a function `decimal_match(n: int, f: float) -> bool` that takes two inputs: a double digit integer `n` and a floating-point number `f` with two decimal digits. The function should return `True` if the decimal part of `f` contains the integer `n` in sequence; otherwise, it should return `False`. 

**Note:** You can assume the integer part will be exactly two digits long, and the decimal part will have exactly two digits.

For example:
- `decimal_match(11, 0.11) → True` because `11` appears in the decimal part of `0.11`. 

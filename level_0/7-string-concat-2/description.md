Strings can also be multiplied by `int`s with `*`!

Say you wanted to print 50 `#`s. Don't ask me why, you wanted to. One way you could accomplish this is to write `print("#")` 50 times, but that would be slow, annoying, and each `#` would be on its own line.

This is where the multiplication comes in handy, you could simply write:
```
pound = "#"
print(pound * 50)
```

Just like that, you have your 50 `#`s, for whatever you wanted them for.

<hr/>

Write a function `str_mult(s, num)` that takes a `str` called `s` and an `int` called `num` as input. This function should return a `str` containing `s`, `num` times.

For example:
- `str_mult("cat", 5)` → `"catcatcatcatcat"`
- `str_mult("gebfcsvfs", 1)` → `"gebfcsvfs"`
- `str_mult(0)` → `""`
Strings share some operators with ints, `+`/`+=` for example.

You can add strings to other strings or multiply them by ints as if you were doing math. This is called <strong>string concatenation</strong>.

For example, say you needed to take two strings and return them as one combined string.
```
string1 = "Hello"
string2 = "World"
combined = s1 + s2

print(combined)
```

This would print `"HelloWorld"`, which works but I want a space between them. This is easy!

```
string1 = "Hello"
string2 = "World"
combined = s1 + " " + s2

print(combined)
```

You can add as many strings together as you want!

<hr/>

Write a function `add_exclamation(s)` that takes a string `s` as input returns the string with '`!`' prepended and appended (added before and after the string).

For example:
- `add_exclamation("hey")` → `!hey!`
- `add_exclamation("wow")` → `!wow!`
- `add_exclamation("")` → `!!`
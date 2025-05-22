Write a function `remove_x_from_start(s: str) -> str` that removes `'x'` characters from the first two characters of a string. Keep the rest of the string as-is. If neither of the first two characters is `'x'`, return the string unchanged.
Examples:
- `"xHi"` → `"Hi"`
- `"Hxi"` → `"Hi"`
- `"Hi"` → `"Hi"`
- `"xxHi"` → `"Hi"`
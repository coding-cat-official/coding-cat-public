Write a function `sandwich_word(s: str) -> str` that returns the substring between the first and last occurrence of the word "bread".

If "bread" does not appear at least twice, return an empty string.

For example:
- `sandwich_word("breadjambread")` → `"jam"`
- `sandwich_word("breadbread")` → `""`
- `sandwich_word("nobreadhere")` → `""`
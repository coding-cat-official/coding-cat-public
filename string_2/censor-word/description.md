Write a function censor_word(s: str, word: str) -> str that replaces every occurrence of `word` in the string `s` with asterisks (`*`), with the same number of asterisks as the length of `word`.

For example:
- `censor_word("this test is a test", "test")` → `"this **** is a ****"`
- `censor_word("bad words are bad", "bad")` → `"*** words are ***"`
- `censor_word("replace nothing", "missing")` → `"replace nothing"`
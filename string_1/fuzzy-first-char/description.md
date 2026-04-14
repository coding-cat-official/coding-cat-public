Write a function `start_word(s: str, word: str) -> str` that does the following:

* Check if the substring of `s` starting from the second character matches the substring from `word` starting from its second character.
* If it matches, return the first part of `s` that has the same length as word.
* If it doesn't match, return an empty string `""`

Examples:
* `("hippo", "hi")` → `"hi"`
* `("hippo", "xip")` → `"hip"`
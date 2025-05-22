Write a function `start_word(s: str, word: str) -> str` that returns the beginning of `s` if `word` **matches** `s` at the front **except** the first character need not match.  
If it matches, return that front portion of `s`; otherwise return an empty string.  
The parameter `word` is at least length 1.  
Examples:
* `("hippo", "hi")` → `"hi"`
* `("hippo", "xip")` → `"hip"`
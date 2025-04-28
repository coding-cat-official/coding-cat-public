Write a function `every_other_repeated(a, b)` that counts how many substrings of length two, formed by taking every other letter from string `a` match the last two letters of string `b`.

For example:
- `every_other_repeated("ooooo", "ooooo")` → `3`
- `every_other_repeated("aabbaa", "baab")` → `2`
- `every_other_repeated("loool", "hello")` → `1`

**Note**: Every other letter means taking the letter, ignoring the one that follows, and taking the next. 
Ex. the sublists of lenght 2 of every other letter in "abcde" **->** "ac", "bd", "ce".

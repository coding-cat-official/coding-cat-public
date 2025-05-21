Write a function `pig_latin(s: str) -> str` that converts each word in the input string `s` to Pig Latin.

Rules for Pig Latin conversion:
- If a word begins with a vowel (a, e, i, o, u), add "way" to the end of the word.
- If a word begins with one or more consonants, move all the leading consonants to the end of the word and add "ay".
- Treat 'y' as a consonant here.
- Preserve the case of the original word (lowercase or uppercase).
- Words are separated by spaces.

For example:
- `pig_latin("apple")` → `"appleway"`
- `pig_latin("strong")` → `"ongstray"`
- `pig_latin("Hello world")` → `"Ellohay orldway"`
Write a function `pyramid_volume(length: int, width: int, height: int) -> str` that determines the volume of a pyramid with a rectangular base using the following formula: `(length x width x height) / 3`

- If the volume of the pyramid is 40 or greater, return: `"That's a big pyramid!"`.
- If the volume of the pyramid is between 25-39 (inclusive), return: `"I mean, it's alright..."`.
- If the volume of the pyramid is less than 25, return: `"Baby pyramid"`.

For example:
- `pyramid_volume(5, 6, 7) → 70 → "That's a big pyramid!"`
- `pyramid_volume(3, 6, 6) → 36 → "I mean, it's alright..."`
- `pyramid_volume(2, 3, 4) → 24 → "Baby pyramid"`

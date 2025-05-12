
Make a function that takes in a string and two characters, and returns how many times the two characters appear next to each other in the string, either directly before or in front of each other. If the string does not contain one of the characters or if both characters are the same, return 0.

Note that pairs should not be double counted. For instance, if we wanted to count how many times "p" appears next to "a" in the word painting, we would only count it once as "pa" and not twice as "pa" and "ap".

For example:
- `count_pairs(“internet”, “t”, “e”) → 2`
- `count_pairs(“policebox”, “b”,  “o”) → 1`
- `count_pairs(“clutter”, “t”, “t”]) → 0`

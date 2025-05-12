
Write a function `first_a_then_b(list_ab: list) -> list` that given a list of strings, returns a new list with all the `"a"`s at the front, then all the `"b"`s. Any other characters (like `"c"`,`"d"`...) must be removed.

For example:
- `first_a_then_b(["a","b","a"])`->`["a","a","b"]`
- `first_a_then_b(["a","d"])`->`["a"]`
- `first_a_then_b(["a","c","a","b","a","a","ab"])`->`["a","a","a","a","b"]`

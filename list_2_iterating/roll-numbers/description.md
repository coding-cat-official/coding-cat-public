You are working as a non-teaching assistant in a school. The principal gives you lists of students for various classes. Your task is to:

1. Rearrange the list in an alphabetical order

2. Create a new list in which each student will have a roll number according to the alphabetical order of their names.

If you get an empty list or an empty string, give the output “Invalid List”. If a string in the list contains numbers or special characters, just treat it like a normal string. But make sure that the list **only** inputs strings and no other variables.

**Hint:** Find a way to arrange the list in an increasing order using built-in python functions

For example:
- `roll_numbers([“James”, “Eric”, “Antman”]) → [[1, “Antman”], [2, “Eric”], [3, “James”]]`
- `roll_numbers([“Khan”, “Singh”, “Maha”, “Karl”]) → [[1, “Karl”], [2, “Khan”], [3, “Maha”], [4, “Singh”]]`
- `roll_numbers([“A”, “Aa”, “a”]) → [[1, “A”], [2, “Aa”], [3, “a”]]`

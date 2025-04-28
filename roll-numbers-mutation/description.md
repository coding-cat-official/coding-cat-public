You are working as a non-teaching assistant in a school. The principal gives you lists of students for various classes. Your task is to rearrange the list in an alphabetical order as well as create a new list in which each student will have a roll number according to the alphabetical order of their names. However, if you get an empty list or empty string (no name or string is empty), give the output “Invalid List”. However, if you see a number or a special character given as inputs as a string, assume that student or those students are named with numbers or special characters. But make sure that the list only inputs strings and no other variables.

For example:
- `assign_roll_numbers([“James”, “Eric”, “Antman”]) → [[1, “Antman”], [2, “Eric”], [3, “James”]]`
- `assign_roll_numbers([“Khan”, “Singh”, “Maha”, “Karl”]) → [[1, “Karl”], [2, “Khan”], [3, “Maha”], [4, “Singh”]]`
- `assign_roll_numbers([“A”, “Aa”, “a”]) → [[1, “A”], [2, “Aa”], [3, “a”]]`

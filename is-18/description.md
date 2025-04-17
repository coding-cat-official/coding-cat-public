Given two strings: `birth_date` and `current_date` (Both in the `YYYY-MM-DD` format), return a Boolean indicating whether or not the person is at least 18 years old currently assuming that today is current_date.

For example:
- `is_18('2007-07-13', '2024-10-29') → False`
- `is_18('2005-10-29', '2024-10-29') → True`
- `is_18('1992-03-24', '1998-06-12') → False`

*Hint:* map() would be useful in this case.
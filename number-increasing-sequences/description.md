Write a function that takes a list of numbers and returns the count of "increasing sequences" in the list. An "increasing sequence" is a consecutive subsequence of elements where each number is greater than or equal to the previous number.

Requirements:
- The function should identify every increasing sequence of consecutive numbers in the list.
- Each increasing sequence must consist of at least one element.
- Count each increasing sequence as a separate entity, even if it consists of only one number.

For example:
- `nbr_increasing_sequences([-0.46, 2.45, -4.0, 23.7]) → 2`
  - Explanation: There are two increasing sequences: `[-0.46, 2.45]` and `[-4.0, 23.7]`.

- `nbr_increasing_sequences([22, 1, 5, -7, 87]) → 3`
  - Explanation: There are three increasing sequences: `[22]`, `[1, 5]`, and `[-7, 87]`.

- `nbr_increasing_sequences([9.46, 0.32, -5.37]) → 3`
  - Explanation: Each element forms its own sequence as there are no consecutive increases: `[9.46]`, `[0.32]`, and `[-5.37]`.

- `nbr_increasing_sequences([9, 0, -5]) → 3`
  - Explanation: Similar to the previous example, each element is its own sequence: `[9]`, `[0]`, and `[-5]`.

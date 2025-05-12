
Write a function `answer_cell(morning: bool, mom: bool, is_asleep: bool) -> bool` that determines whether you should answer your cell phone based on the following conditions:

- Normally, you answer the phone except when you are asleep.
- In the morning, you only answer if it is your mom calling.
- If you are asleep, you do not answer the phone regardless of the time or who is calling.

Return `True` if you should answer the phone and `False` otherwise.

For example:
- If `morning` is `false`, `mom` is `false`, and `is_asleep` is `false`, you should answer, so the output is `true`.
- If `morning` is `false`, `mom` is `false`, and `is_asleep` is `true`, you should not answer because you are asleep, so the output is `false`.
- If `morning` is `true`, `mom` is `false`, and `is_asleep` is `false`, you should not answer because it is not your mom calling, so the output is `false`.

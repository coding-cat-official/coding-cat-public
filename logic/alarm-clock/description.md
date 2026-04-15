Write a function `alarm_clock(day: int, vacation: bool) -> str` that takes in a day of the week (encoded as 0=Sunday, 1=Monday, ..., 6=Saturday) and a boolean indicating whether or not you are on vacation. The function should return a string representing what time the alarm should ring.

The alarm clock rules are:
- On weekdays (Monday–Friday), the alarm should be "7:00".
- On weekends (Saturday and Sunday), the alarm should be "10:00".
- If you are on vacation:
  - Weekdays: "10:00"
  - Weekends: "off"

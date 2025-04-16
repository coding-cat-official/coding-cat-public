You want to calculate your final grade for Discrete Math. Your teacher informs you that the two lowest test scores will be discarded from your six tests for your final grade. 

Given a list of integers from range of 0 to 100 with a length of 6, remove the two lowest value and then calculate your average for the remaining 4 marks. However, if have a failing final grade (under 60) or if you are missing a test, your mark will automatically be 0. 

*Note:* Round the average to the nearest integer.

For example:
- `final_grade([90, 90, 85, 87, 80, 100]) → 92`
- `final_grade([36, 56, 70, 0, 55, 50]) → 0`
- `final_grade([100, 100, 100, 100, 95]) → 0`

**Hint:** Find a way to arrange the list in an increasing order
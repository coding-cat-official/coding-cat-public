A very useful math operator to know about in coding is `%`, the Modulus Operator.

Also called the remainder operator, it is used to get the remainder of the division of two `int`s. It can be used just like any other math operator.
Example:
```
10 % 5 = 0 (10 divides cleanly by 5 with no remainder, so 0)
7 % 3 = 1 (7 can be divided into 2 groups of 3, leaving a remainder of 1)
6 % 10 = 6 (6 can't make one full group of 10, leaving a remainder of the whole 6)
```

For more information on Modulus, check out [this blog post]()

<hr/>

For this problem, you are a baker who bakes doughnuts. You ship them in boxes of 12. 

Write a function `get_remaining_doughnuts(doughtnuts)` that takes an `int` representing a number of doughnuts, and returns an `int` representing the number of doughnuts remaining after you fill as many boxes of 12 as you can.

For example:
- `get_remaining_doughnuts(48)` → `0` (48 goes cleanly into dozens, 0 remaining)
- `get_remaining_doughnuts(13)` → `1` (13 makes one dozen, with 1 remaining)
- `get_remaining_doughnuts(5)` → `5` (5 doesn't fill a dozen, so 5 remaining)
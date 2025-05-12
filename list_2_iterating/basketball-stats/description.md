
Imagine you have to calculate the stats of a basketball player after a game. You have the player’s amount of 2-pointers and 3-pointers made, as well as the total amount of shots they took. 

Calculate how many total points they have, as well as their FG% (shots made / shots taken, as a percentage), with no decimals, and rounded down. 

Example: `"66.666%" = "66%"`
(Hint: `import math`, then use `math.floor()`)

Write a function `bball_stats(twos: int, threes: int, shotsTaken: int)` that takes three integer inputs, `twos`, `threes`, and `shotsTaken`.

Return a list with an `int` and a `str`, where the `int` is their total amount of points and the `str` is the field goal percentage as a number with a percent. 

Examples:

- `bball_stats(1, 1, 2) == [5, "100%"]`
1 two-pointer and 1 three-pointer = 5 points. The player took 2 shots, but also made 2 shots, so their FG% is 100%.

- `bball_stats(0, 0, 5) == [0, "0%"]`
0 two-pointers and 0 three-pointers = 0 points. The player took 5 shots, but made 0 shots, so their FG% is 0%.

- `bball_stats(2, 0, 3) == [4, "66%"]`
2 two-pointers and 0 three-pointers = 4 points. The player took 3 shots, but made 2 shots, so their FG% is 66%.

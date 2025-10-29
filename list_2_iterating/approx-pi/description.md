Write a function `approx_pi(n)` that takes in an integer `n` and returns a list of terms from the Leibniz approximation series for pi up to `n` terms. 

The Leibniz formula for approximating pi is:

`pi = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - ... )`

Each term in the series has the form `4 / (2 * i + 1)` where `i` is the index of the term, starting from 0. For example, the first term is `4/1`, the second term is `-4/3`, the third term is `4/5`, and so on. The terms alternate in sign.

Your function should return a list of the first `n` terms in the series, rounded to 5 decimal places.

For example:
- `approx_pi(1)` should return `[4.0]`
- `approx_pi(2)` should return `[4.0, -1.33333]`
- `approx_pi(5)` should return `[4.0, -1.33333, 0.8, -0.57143, 0.44444]`

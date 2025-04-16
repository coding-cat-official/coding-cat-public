
Write a function `pull_primes(list)`, where the list contains 4 positive integers between 0 and 169 (not included), that determines if any of the numbers are primes and adds them to the list `only_primes` that includes only the primes (make sure that the primes are in ascending order), if there are none, return `There are no prime numbers in this list`.
For the sake of simplicity, assume that we only care for the prime factors 2, 3, 5, 7 and 11

For example:
- `pull_primes([1, 3, 12, 14])` → `[1, 3]`
- `pull_primes([12, 13, 41, 62])` → `[13, 41]`
- `pull_primes([12, 14, 16, 18])` → `There are no prime numbers in this list`

**Hint:** Modulo is required

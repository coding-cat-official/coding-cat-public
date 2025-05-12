import math

def make_series_mutation(n: int) -> float:
    a = 1
    for _ in range(n):
        a = 3 * math.sqrt(a)
    return a
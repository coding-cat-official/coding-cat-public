import math

def series(n: int) -> float:
    a = 1
    for _ in range(n):
        a = round(3 * math.sqrt(a), 3)
    return a
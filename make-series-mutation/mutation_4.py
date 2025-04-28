import math

def series(n: int) -> float:
    for i in range(n):
        i = round(3 * math.sqrt(i), 3)
    return i
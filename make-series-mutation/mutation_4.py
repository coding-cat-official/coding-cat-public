import math

def make_series_mutation(n: int) -> float:
    for i in range(n):
        i = round(3 * math.sqrt(i), 3)
    return i
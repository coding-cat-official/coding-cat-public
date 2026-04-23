def range_chars(a: str, b: str) -> str:
  """
  Buggy Mutation: The buggy mutation subtracts 1 from len(b)
  This will unnecessarily reduce  the range of iterations skipping valid some comparisons
  """
    result = ""
    n = min(len(a), len(b)-1)
    for i in range(n):
        if (i > 0 and a[i] == b[i-1]) or a[i] == b[i] or (i < n - 1 and a[i] == b[i+1]):
            result += a[i]
    return result

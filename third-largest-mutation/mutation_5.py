def third_largest_mutation(numbers):
  '''
    Reversing and selecting the element at index 3 (position 4) instead of index 2 (position 3)
  '''
  if len(numbers) < 4:
    return "This list is too short"

  return list(reversed(sorted(numbers)))[3]

def third_largest_mutation(numbers):
  '''
    Using <= instead of <
  '''
  if len(numbers) <= 4:
    return "This list is too short"

  return sorted(numbers)[-3]

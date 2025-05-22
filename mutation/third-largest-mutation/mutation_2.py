def third_largest_mutation(numbers):
  '''
    Selecting the 3rd smallest instead of largest
  '''
  if len(numbers) < 4:
    return "This list is too short"

  return sorted(numbers)[2]

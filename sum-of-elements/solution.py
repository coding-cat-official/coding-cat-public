def unique_sum(lst):
  unique_elements = set()
  duplicates = set()
  
  for num in lst:
    if num in unique_elements: """If the number is already unique, it becomes a duplicate"""
      unique_elements.remove(num)
      duplicates.add(num)
    elif num not in duplicates: """If it's not a duplicate and not yet unique, add it"""
      unique_elements.add(num)
  return sum(unique_elements) """Sum all elements that are unique"""

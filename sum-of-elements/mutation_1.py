def unique_sum(lst):
    unique_elements = set()
    duplicates = set()
    for num in lst:
        if num in unique_elements:
            unique_elements.remove(num)
            duplicates.add(num)
        elif num not in duplicate:
            unique_elements.add(num)
        return sum(unique_elements) 
        """This won't work since the return function is in the loop"""

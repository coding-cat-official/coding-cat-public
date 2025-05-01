def unique_sum(lst):
    unique_elements = set()
    duplicates = set()
    for num in lst:
        if num in unique_elements.remove(num):
            unique_elements.remove(num)
            duplicates.add(num)
        elif num not in duplicates:
            unqiue_elements.add(num)
    return(unique_elements)
    """It won't work since it will just return the list of unique elements and not the sum"""

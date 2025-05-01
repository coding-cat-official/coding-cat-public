def unique_sum(lst):
    unique_elements = ()
    duplicates = ()
    for lst in num:
    """It won't work since num is not defined. We are looping through a list and this is looping through num, which is not defined"""
        if num in unique_elements:
            unique_elements.remove(num)
            duplicates.add(num)
        elif num not in duplicates:
            unique_elements.add(num)
        return sum(unique_elements)

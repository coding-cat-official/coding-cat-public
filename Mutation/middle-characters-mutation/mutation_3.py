def middle_characters_mutation(s):
    '''
    Incorrectly modifying the count
    This mutation incorrectly modifies the count by decrementing it instead of incrementing it when a match is found.
    '''
    s = s.lower()  # Convert the string to lowercase to handle case insensitivity
    first_char = s[0]
    count = 0
    for char in s[1:-1]:  # Exclude the first and last characters
        if char == first_char:
            count -= 1  # Mutated: incorrect count modification
    return count

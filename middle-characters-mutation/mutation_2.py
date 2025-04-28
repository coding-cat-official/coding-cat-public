def middle_characters(s):
    '''
    Off-by-one error in loop boundary
    This mutation does not exclude the last character from the loop, causing it to incorrectly count the last character if it matches the first character.
    '''
    s = s.lower()  # Convert the string to lowercase to handle case insensitivity
    first_char = s[0]
    count = 0
    for char in s[1:]:  # Mutated: does not exclude the last character
        if char == first_char:
            count += 1
    return count

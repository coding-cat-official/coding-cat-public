def middle_characters_mutation(s):
    '''
    Correct implementation
    '''
    s = s.lower()  # Convert the string to lowercase to handle case insensitivity
    first_char = s[0]
    count = 0
    for char in s[1:-1]:  # Exclude the first and last characters
        if char == first_char:
            count += 1
    return count

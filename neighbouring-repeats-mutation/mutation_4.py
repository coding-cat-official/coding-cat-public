def neighbour_repeat(word: str) -> str:
    '''
    Forgot to look backwards in the for loop
    '''
    new_word = ""
    if len(word) == 1:
        return word
    for i in range(len(word)-1): # Should start at index 1
        if word[i] != word[i+1]: # Should check the letter before
            new_word += word[i]
    if len(word) > 1:
        if word[-1] != word[-2]:
            new_word += word[-1]
    return new_word

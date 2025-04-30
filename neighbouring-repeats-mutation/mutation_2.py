def neighbouring_repeats_mutation(word: str) -> str:
    '''
    Forgot to stricten the loop boundary, it should start at the second letter
    '''
    new_word = ""
    if len(word) == 1:
        return word
    elif len(word) == 2:
        if word[0] == word[1]:
            return new_word
        return word
    for i in range(len(word)-1): # The indexing should start at 1
        if word[i] != word[i-1] and word[i] != word[i+1]:
            new_word += word[i]
    if len(word) > 2:
        if word[-1] != word[-2]:
            new_word += word[-1]
        if word[0] != word[1]:
            return word[0] + new_word
    return new_word

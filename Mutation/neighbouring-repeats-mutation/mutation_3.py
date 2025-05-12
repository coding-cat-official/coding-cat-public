def neighbouring_repeats_mutation(word: str) -> str:
    '''
    Forgot to add a check for words of length 2
    '''
    new_word = ""
    # Check for words of length 2 should be here 
    if len(word) == 1:
        return word
    for i in range(1, len(word)-1):
        if word[i] != word[i-1] and word[i] != word[i+1]:
            new_word += word[i]
    if len(word) > 2:
        if word[-1] != word[-2]:
            new_word += word[-1]
        if word[0] != word[1]:
            return word[0] + new_word
    return new_word

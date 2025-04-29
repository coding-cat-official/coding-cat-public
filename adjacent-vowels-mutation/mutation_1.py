def adjacent_vowels_mutation(word: str) -> int:
    '''
    wrong condition check at the if statement :
    if word[index]  (omitted in vowels)
    '''
    count = 0
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    for index in range(len(word)-1):
        if word[index] and word[index + 1] in vowels:
            count += 1

    return count


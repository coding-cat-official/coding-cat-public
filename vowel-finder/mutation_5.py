from typing import List

def vowel_finder(input: str) -> List[str]:
    '''
        Checks for anything that isn't a vowel.
    '''
    vowels = "aeiouyAEIOUY"
    vowel_found = []
    for i in input:
        if i not in vowels:
            vowel_found.append(i)
    return vowel_found

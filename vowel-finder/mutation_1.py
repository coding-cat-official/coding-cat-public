from typing import List

def vowel_finder(input: str) -> List[str]:
    '''
        Does not check for the i and I vowels.
    '''
    vowels = "aeouyAEOUY"
    vowel_found = []
    for i in input:
        if i in vowels:
            vowel_found.append(i)
    return vowel_found

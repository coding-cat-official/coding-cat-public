from typing import List

def vowel_finder(input: str) -> List[str]:
    '''
        Only considers unique vowels.
    '''
    vowels = "aeiouyAEIOUY"
    vowel_found = []
    for i in input:
        if i in vowels and i not in vowel_found:
            vowel_found.append(i)
    return vowel_found

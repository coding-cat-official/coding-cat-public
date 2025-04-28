from typing import List

def vowel_finder(input: str) -> List[str]:
    '''
        All uppercase vowels are not considered.
    '''
    vowels = "aeiouy"
    vowel_found = []
    for i in input:
        if i in vowels:
            vowel_found.append(i)
    return vowel_found

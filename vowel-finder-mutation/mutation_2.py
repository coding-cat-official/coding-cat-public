from typing import List

def vowel_finder_mutation(input: str) -> List[str]:
    '''
        Return statement placed incorrectly.
    '''
    vowels = "aeiouyAEIOUY"
    vowel_found = []
    for i in input:
        if i in vowels:
            vowel_found.append(i)
            return vowel_found

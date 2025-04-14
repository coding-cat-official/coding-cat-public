from typing import List

def vowel_finder(input: str) -> List[str]:
    vowels = "aeiouyAEIOUY"
    vowel_found = []
    for i in input:
        if i in vowels:
            vowel_found.append(i)
    return vowel_found

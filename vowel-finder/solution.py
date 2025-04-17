from typing import List

def vowel_finder(s: str) -> List[str]:
    vowels = "aeiouyAEIOUY"
    vowel_found = []
    for i in s:
        if i in vowels:
            vowel_found.append(i)
    return vowel_found

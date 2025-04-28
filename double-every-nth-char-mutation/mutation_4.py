def mutation_2(text: str, n: int) -> str:
    '''
    Incorrect character multiplication, the function will triple the characters at the specified positions (rather than doubling them).
    '''
    result = []
    for i, char in enumerate(text, start=1):
        if i % n == 0:
            result.append(char * 3)  # Mutated: changed '* 2' to '* 3'
        else:
            result.append(char)
    return ''.join(result)

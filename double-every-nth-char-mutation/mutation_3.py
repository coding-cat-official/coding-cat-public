def double_nth_char(text: str, n: int) -> str:
    """
    Missing, start = 1 . Without it, the indexing will start at 0 (default behavior), and the positions checked in the condition if i % n == 0 will be 0-based indices instead of the 1-based positions described in the problem.
    """
    result = []
    for i, char in enumerate(text): 
        if i % n == 0:  
            result.append(char * 2)  
        else:
            result.append(char)
    return ''.join(result)

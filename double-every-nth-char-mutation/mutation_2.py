def double_every_nth_char_mutation(text: str, n: int) -> str:
    """
        Incorrect comparaison operator, != instead of == in the condition if i % n == 0, will invert the logic, and the function will double every character except those at positions that are multiples of n.
    """
    result = []
    for i, char in enumerate(text, start=1): 
        if i % n != 0:  
            result.append(char * 2)  
        else:
            result.append(char)
    return ''.join(result)

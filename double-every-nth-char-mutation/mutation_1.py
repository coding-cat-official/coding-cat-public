def double_nth_char(text: str, n: int) -> str:
    """
        Incorrect use of str() function to convert list into string (still returns it as a list instead of a string)
    """
    result = []
    for i, char in enumerate(text, start=1): 
        if i % n == 0:  
            result.append(char * 2)  
        else:
            result.append(char)
    return str(result)
    

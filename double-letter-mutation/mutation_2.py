def double_letter(word):
    '''
        Limiting the iteration to len(result)-2, 
        the loop will ignore the last two characters of the string
    '''
    consonants = "bcdfghjklpmntrqsvwxyzBCDFGHJKLMNPQRSTVWXYZ"  
    consonant_count = 0 
    result = list(word) 

    for i in range(len(result)-2):
        if result[i] in consonants:
            consonant_count += 1
            if consonant_count == 2: 
                result[i] = result[i] * 2 
                break 
    return "".join(result) 
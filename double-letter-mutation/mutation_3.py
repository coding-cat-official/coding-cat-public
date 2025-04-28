def double_letter(word):
    '''
        Change comparison logic, "if result not in consonants"
        will cause the code to look at non-consonant characters instead
    ''' 
    consonants = "bcdfghjklpmntrqsvwxyzBCDFGHJKLMNPQRSTVWXYZ"  
    consonant_count = 0 
    result = list(word) 

    for i in range(len(result)):
        if result[i] not in consonants: #Wrong comparison
            consonant_count += 1
            if consonant_count == 2: 
                result[i] = result[i] * 2 
                break 
    return "".join(result) 
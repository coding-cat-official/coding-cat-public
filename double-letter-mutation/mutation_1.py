def double_letter_mutation(word):
    '''
        Simple Mistake, missing consonants (c,t,n)
    '''
    consonants = "bdfghjklpmrqsvwxyzBCDFGHJKLMNPQRSTVWXYZ"  
    consonant_count = 0 
    result = list(word) 

    for i in range(len(result)):
        if result[i] in consonants:
            consonant_count += 1
            if consonant_count == 2: 
                result[i] = result[i] * 2 
                break 
    return "".join(result) 
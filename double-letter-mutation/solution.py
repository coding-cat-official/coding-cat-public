def double_letter_mutation(word):
    '''
        Correct implementation
    '''
    consonants = "bcdfghjklpmntrqsvwxyzBCDFGHJKLMNPQRSTVWXYZ"  # List of consonants (both upper and lower case)
    consonant_count = 0 # To count consonants found
    result = list(word) # convert string to list for easier manipulation

    for i in range(len(result)):
        if result[i] in consonants:
            consonant_count += 1
            if consonant_count == 2: # When we find the second consonant
                result[i] = result[i] * 2 # Double the second consonant
                break # We can stop as we've made the necessary change
    return "".join(result) #join the list back into a string
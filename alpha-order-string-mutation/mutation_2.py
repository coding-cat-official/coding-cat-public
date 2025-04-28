def alpha_order(word : str) -> str:
	'''
	    Incorrectly modify first for loop boundary
	'''
        new_word = ""
        word = list(word)
        for n in range(len(word)-2): #Mutated loop limit
                for n in range(len(word)-1):
                        if word[n] > word[n+1]:
                                word[n+1], word[n] = word[n], word[n+1]
        for n in range(len(word)):
                new_word += word[n]
        return new_word

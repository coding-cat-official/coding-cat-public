def alpha_order(word : str) -> str:
        '''
            Start the first loop from index 1 instead of 0
        '''
        new_word = ""
        word = list(word)
        for n in range(1, len(word)-1):
                for n in range(len(word)-1):
                        if word[n] > word[n+1]:
                                word[n+1], word[n] = word[n], word[n+1]
        for n in range(len(word)):
                new_word += word[n]
        return new_word

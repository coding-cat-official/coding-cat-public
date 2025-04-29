def count_vowels_mutation(string):
    lst = []
    for i in string:
        if i in ['aeiouyAEIOUY']:
            lst.append(i)
    return len(lst)
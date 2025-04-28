def count_vowels(string):
    lst = []
    for i in string:
        if i in ['aeiouyAEIOUY']:
            lst.append(i)
    return len(lst)
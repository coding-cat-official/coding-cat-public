def count_vowels(string):
    lst = []
    for i in string:
        if i in ['a','i','e','o','u','y',]: #didn't include capitals, therfore not generalized
            lst.append(i)
    return len(lst)
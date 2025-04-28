def count_vowels(string):
    lst = []
    for i in string:
        if i in ['a','i','e','o','u','A','I','E','O','U','Y']: #forget a vowel
            lst.append(i)
    return len(lst)

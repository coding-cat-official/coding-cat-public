def count_vowels(string):
    lst = []
    for i in string:
        if i in ['a','i','e','o','u','y','A','I','E','O','U','Y']:
            lst.append(i)
    return len(lst)

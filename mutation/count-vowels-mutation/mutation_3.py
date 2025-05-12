def count_vowels_mutation(string):
    lst = []
    for i in range(len(string)): #taking the range of the string instead of elements of the string
        if i in ['a','i','e','o','u','y','A','I','E','O','U','Y']:
            lst.append(i)
    return len(lst)
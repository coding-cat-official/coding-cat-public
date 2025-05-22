def reverse_string_mutation(string):
    '''
By doing reversed_s += char, it just duplicated the original string instead of changing the order.
'''

    reversed_s = ""
    for char in string:
        reversed_s += char
    return reversed_s

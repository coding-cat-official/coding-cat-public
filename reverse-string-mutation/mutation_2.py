def reverse_string(string):
    '''
    Simple mistake, this skips over the last letter
'''

    reversed_s = ""
    for char in string[:-1]:
        reversed_s = char + reversed_s
    return reversed_s

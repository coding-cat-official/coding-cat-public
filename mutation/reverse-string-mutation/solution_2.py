def reverse_string_mutation(string):
    reversed_s = ""
    for char in string:
        reversed_s = char + reversed_s
    return reversed_s

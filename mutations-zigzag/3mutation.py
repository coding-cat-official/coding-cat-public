def zig_zag(s):
    s = list(s)
    result = ""
    for i in range(len(s)):
        if i % 2 == 0:
            s.pop(0)  # Pop from the front without adding to result
        else:
            result += s.pop(-1)  # Only add from the end
    return result
"""This mutation skips all characters from the front of the list and only adds characters from the back.""" 

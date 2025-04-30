def zig_zag(s):
    '''
    The zig-zag logic is inverted
    '''
    s = list(s)
    result = ""
    for i in range(len(s)):
        if i % 2 == 0:
            result += s.pop(-1)  # Remove from the end instead of the beginning
        else:
            result += s.pop(0)  # Remove from the beginning instead of the end
    return result

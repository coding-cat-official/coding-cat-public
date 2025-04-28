def longest_common_substring(a, b):
    '''
        wrong comparing symbols.
    '''
    max_len = 0
    for i in range(len(a)):
        for j in range(len(b)):
            length = 0
            while i + length > len(a) and j + length > len(b) and a[i + length] == b[j+ length]:
                length += 1
            max_len = max(max_len, length)
    return max_len

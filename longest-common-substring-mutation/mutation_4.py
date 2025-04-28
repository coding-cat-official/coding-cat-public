def longest_common_substring(a, b):
    '''
        (using solution2) omitting +1 in the two entities of the range
    '''
    max_len = 0
    for i in range(len(a)):
        for j in range(i, len(a)):
            substring = a[i:j]
            if substring in b:
                max_len = max(max_len, j - i)
    return max_len

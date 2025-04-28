def longest_common_substring(a, b):
    '''
        (using solution2) omit -1 in j when comparing max_len and j
    '''
    max_len = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a) + 1):
            substring = a[i:j]
            if substring in b:
                max_len = max(max_len, j)
    return max_len

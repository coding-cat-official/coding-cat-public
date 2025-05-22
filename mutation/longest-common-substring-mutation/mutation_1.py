def longest_common_substring_mutation(a,b):
    '''
        Omitting i & j in the index for a & b in the while loop
    '''
    max_len = 0
    for i in range(len(a)):
        for j in range(len(b)):
            length = 0
            while i + length < len(a) and j + length < len(b) and a[length] == b[length]:
                length += 1
            max_len = max(max_len, length)
    return max_len

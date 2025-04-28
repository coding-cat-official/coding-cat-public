def every_other_repeated(a, b):
    count = 0

    for i in range(len(a) - 2):
        if a[i] + a[i+2] == b[-2:]:
            count += 1
    return count

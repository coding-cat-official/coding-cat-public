def make_fibonacci(n: int):
    '''
        Mutation 2: range has wrong end value, should be range(2,n) instead of range(2,n-1)
    '''
    if n == 0:
        return []
    elif n == 1:
        return [0]
    fibo = [0,1]
    for x in range(2,n-1):
        fibo.append(fibo[-1]+fibo[-2])
    return fibo

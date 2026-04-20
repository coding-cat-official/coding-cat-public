def make_fibonacci(n: int):
    '''
        Mutation 3: wrong starting range, so will output too many fibo numbers. Should be range(2,n) instead of range(0,n)
    '''
    if n == 0:
        return []
    elif n == 1:
        return [0]
    fibo = [0,1]
    for x in range(0,n):
        fibo.append(fibo[-1]+fibo[-2])
    return fibo

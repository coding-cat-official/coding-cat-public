def make_fibonacci(n: int):
    '''
        Mutation 1: missing case for n == 0, will return [0,1] instead of []
    '''
    if n == 1:
        return [0]
    fibo = [0,1]
    for x in range(2,n):
        fibo.append(fibo[-1]+fibo[-2])
    return fibo

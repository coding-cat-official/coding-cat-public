def make_fibonacci(n: int):
    '''
        Correct solution
    '''
    if n == 0:
        return []
    elif n == 1:
        return [0]
    fibo = [0,1]
    for x in range(2,n):
        fibo.append(fibo[-1]+fibo[-2])
    return fibo

def make_fibonacci(n: int):
    '''
        Mutation 4: wrong initial value, should be [0,1] instead of [1,1]. This outputs an incorrect recursive relation.
    '''
    if n == 0:
        return []
    elif n == 1:
        return [0]
    fibo = [1,1]
    for x in range(2,n):
        fibo.append(fibo[-1]+fibo[-2])
    return fibo

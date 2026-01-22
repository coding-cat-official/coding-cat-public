def make_fibonacci(n: int):
    '''
        Mutation 5: the line that appends fibo[-1] + fibo[-2] has the wrong index values, so instead of recursively adding fibonacci numbers, it just adds additional 1s
    '''
    if n == 0:
        return []
    elif n == 1:
        return [0]
    fibo = [0,1]
    for x in range(2,n):
        fibo.append(fibo[0]+fibo[1])
    return fibo

def fibo_lessthan(n):
    
    #Incorrect starting numbers

    fibolist = []
    a, b = 1, 2
    if n % 1 == 0 and n >= 0:
        while a <= n:
            
                print(a, end=' ')
                fibolist.append(a)
                a, b = b, a + b
        return fibolist
    else:
        print("No")
        return False

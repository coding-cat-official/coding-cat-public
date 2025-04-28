def fibo_lessthan(n):

    #Not filtering non-positive integers and non-integers

    fibolist = []
    a, b = 0, 1
    while a <= n:
            
                print(a, end=' ')
                fibolist.append(a)
                a, b = b, a + b
                return fibolist
    else:
        print("No")
        return False
      

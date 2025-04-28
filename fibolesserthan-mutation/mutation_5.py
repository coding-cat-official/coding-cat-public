def fibo_lessthan(n):

    #Appending wrong element

    fibolist = []
    a, b = 0, 1
    if n % 1 == 0 and n >= 0:
        while a <= n:
            
                print(a, end=' ')
                fibolist.append(b)
                a, b = b, a + b
        return fibolist
    else:
        print("No")
        return False

      

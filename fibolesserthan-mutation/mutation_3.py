def fibo_lessthan(n):
    
    #Returning wrong values
    fibolist = []
    a, b = 0, 1
    if n % 1 == 0 and n >= 0:
        while a <= n:
            
                print(a, end=' ')
                fibolist.append(a)
                a, b = b, a + b
        return a, b
    else:
        print("No")
        return False
      

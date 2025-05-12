def fibolesserthan_mutation(n):

    #Making a strictly smaller than n; fibo_upto(1) will return 0, instead of 0, 1, 1. 
    fibolist = []
    a, b = 0, 1
    if n % 1 == 0 and n >= 0:
        while a < n:
            
                print(a, end=' ')
                fibolist.append(a)
                a, b = b, a + b
        return fibolist
    else:
        print("No")
        return False
    

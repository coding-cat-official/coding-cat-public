def list_equate_mutation(list1, list2):
    """
    Mistakenly puts temptrue before the "for i" loop.
    This makes it so that so long as the first element is found in the other list, the program will always return 'True'.
    This happens regardless if the other elements are correct, as temptrue is stuck as 'True' until the program switches the lists.
    """
    for _ in range(2):
        temptrue = False #mutated to be before "for i in list1" instead of after it
        for i in list1:
            for j in list2:
                if i == j:
                    temptrue = True 
            if temptrue == False:
                return False
        list1, list2 = list2, list1
    return True
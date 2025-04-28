def list_equate(list1, list2):
    """
    Forgets to iterate over both lists, and instead the program will just iterate over only one list
    """
    #mutated to remove the looping twice
    for i in list1:
        temptrue = False
        for j in list2:
            if i == j:
                temptrue = True 
        if temptrue == False:
            return False
    #mutated to remove the switching between the two lists
    return True
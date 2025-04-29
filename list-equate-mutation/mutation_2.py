def list_equate_mutation(list1, list2):
    """
    Second for-in loop is iterating over list1 by accident instead of list2
    """
    for _ in range(2):
        for i in list1:
            temptrue = False
            for j in list1: #mutated to be list1 instead of list2
                if i == j:
                    temptrue = True 
            if temptrue == False:
                return False
        list1, list2 = list2, list1
    return True
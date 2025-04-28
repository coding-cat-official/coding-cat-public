def list_equate(list1, list2):
    """
    Flips temptrue and temptrue statements, seemingly normal.
    Would make it so that if the lists aren't the same number repeated over again, the lists do not equate.
    temptrue would turn 'False' as soon as a single number in the list wasn't the same as whatever 'i' was found.
    """
    for _ in range(2):
        for i in list1:
            temptrue = True #mutated to be true
            for j in list2:
                if i != j: #mutated to be does not equal to instead of equals to
                    temptrue = False #mutated to transform into false
            if temptrue == False: #mutated to check for false temptrue
                return False
        list1, list2 = list2, list1
    return True
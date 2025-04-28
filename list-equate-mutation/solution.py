def list_equate(list1, list2):
    for _ in range(2):
        for i in list1:
            temptrue = False
            for j in list2:
                if i == j:
                    temptrue = True 
            if temptrue == False:
                return False
        list1, list2 = list2, list1
    return True
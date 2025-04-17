def four_two_relationship(lst):
    '''
        Instead of putting ==, put !=
    '''
    find_2=False
    find_4=False
    for number in lst:
        if number==2:
            find_2=True
        if number==4:
            find_4=True
    if find_2 and find_4:
        for i in range(len(lst) - 1):
            if (lst[i] == 2 and lst[i + 1] != 4) or (lst[i] == 4 and lst[i + 1] != 2):
                return False
        return True
    return False

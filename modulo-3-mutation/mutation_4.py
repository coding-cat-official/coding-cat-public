def modulo_3(str:str) -> str:
    """
    Incorrect 'for loop' iteration boundary(short by 3)
    """
    list1=[]
    list2=[]
    list3=[]
    for x,char in enumerate(str[:-3]):#this is not a look-forward so it is not needed to modify the 'for loop' boundary.
        if x%3==0:
            list1.append(char)
        if x%3==1:
            list2.append(char)
        if x%3==2:
            list3.append(char)
    return "".join(list1+list2+list3)

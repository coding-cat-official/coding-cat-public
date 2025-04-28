def modulo_3(str:str) -> str:
    """
    forgot to join the lists
    """
    list1=[]
    list2=[]
    list3=[]
    for x, char in enumerate(str):
        if x%3==0:
            list1.append(char)
        if x%3==1:
            list2.append(char)
        if x%3==2:
            list3.append(char)
    return list1+list2+list3#Join the lists to a string here

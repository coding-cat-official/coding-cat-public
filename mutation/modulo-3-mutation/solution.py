def modulo_3_mutation(str:str) -> str:
    """
    the correct implementation
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
    return "".join(list1+list2+list3)

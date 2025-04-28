def modulo_3(str:str) -> str:
    """
    Incorrect remainders used in modular operation
    """
    list1=[]
    list2=[]
    list3=[]
    for x, char in enumerate(str):
        if x%3==1:#the remainder should start at 0 and be up to 2
            list1.append(char)
        if x%3==2:
            list2.append(char)
        if x%3==3:
            list3.append(char)
    return "".join(list1+list2+list3)

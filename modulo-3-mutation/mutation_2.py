def modulo_3(str:str) -> str:
    """wrong operator used for indexing"""
    list1=[]
    list2=[]
    list3=[]
    for x, char  in enumerate(str):
        if x//3==0:#Use the modular operator in place of the integer division operator
            list1.append(char)
        if x//3==1:
            list2.append(char)
        if x//3==2:
            list3.append(char)
    return "".join(list1+list2+list3)

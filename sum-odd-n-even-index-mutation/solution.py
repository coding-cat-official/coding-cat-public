def sum_oddneven_list(input_list):
    output = 0
    if(len(input_list) % 2 == 0):
        for i in range(len(input_list)):
            if i % 2 != 0:
                output += input_list[i]
    else:
        for i in range(len(input_list)):
            if i % 2 == 0:
                output += input_list[i]
    return output

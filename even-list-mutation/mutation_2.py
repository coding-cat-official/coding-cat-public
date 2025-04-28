def even_list(numbers):
    '''
    simple mistake, forgot to append num into the even numbers and just returned num.
'''
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            return num  # mutation: returned num and didn't append into even_numbers list

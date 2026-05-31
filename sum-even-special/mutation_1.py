def is_prime(n):
    '''
        Always returns that the number is prime
    '''
    return True
    
def sum_even_special(lst):
    total_sum = 0
    for num in lst:
        if num % 2 == 0 and (is_prime(num) or num % 3 == 0):
            total_sum += num
    return total_sum
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def sum_even_special(lst):
    total_sum = 0
    for num in lst :
        if is_prime(num):
            '''
                Not checking for divisible by 3
            '''
            total_sum += num
    return total_sum
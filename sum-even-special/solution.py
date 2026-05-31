def is_prime(n):
    if n <= 1:
        return False
    for i in range (2,n):
        if n % i == 0:
            return False
    return True
def sum_even_special(lst):
    total_sum = 0
    for num in lst:
        if num % 2 == 0 and (is_prime(num) or (num%3) == 0):
            total_sum += num
    return total_sum
def is_18(birth_date: str, current_date: str) -> bool:
    '''
    Mutation 3: Swaps month and day when comparing dates, leading to incorrect age calculation.
    '''

    birth_year, birth_month, birth_day = map(int, birth_date.split('-'))
    current_year, current_month, current_day = map(int, current_date.split('-'))

    age = current_year - birth_year

    # Incorrectly swaps month and day in comparison
    if (current_day, current_month) < (birth_month, birth_day):
        age -= 1

    return age >= 18

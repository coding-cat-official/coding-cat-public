def is_18(birth_date: str, current_date: str) -> bool:
    '''
    Mutation 5: Incorrectly requires age to be greater than 18 instead of at least 18.
    '''

    birth_year, birth_month, birth_day = map(int, birth_date.split('-'))
    current_year, current_month, current_day = map(int, current_date.split('-'))

    age = current_year - birth_year

    if (current_month, current_day) < (birth_month, birth_day):
        age -= 1

    return age > 18  # Should be >= 18

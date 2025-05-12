def is_18_mutation(birth_date: str, current_date: str) -> bool:
    '''
    Mutation 4: Incorrectly decrements age when current date is exactly the birthday.
    '''

    birth_year, birth_month, birth_day = map(int, birth_date.split('-'))
    current_year, current_month, current_day = map(int, current_date.split('-'))

    age = current_year - birth_year

    # Incorrect comparison: should not decrement age if current date is the birthday
    if (current_month, current_day) <= (birth_month, birth_day):
        age -= 1

    return age >= 18

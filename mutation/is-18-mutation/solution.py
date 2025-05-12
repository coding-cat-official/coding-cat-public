def is_18_mutation(birth_date: str, current_date: str) -> bool:
    """
    Determines if a person is 18 years or older based on their birth date.
    """

    birth_year, birth_month, birth_day = map(int, birth_date.split("-"))
    current_year, current_month, current_day = map(int, current_date.split("-"))

    age = current_year - birth_year

    if (current_month, current_day) < (
        birth_month,
        birth_day,
    ):  # Birthday hasn't occurred this year
        age -= 1

    return age >= 18

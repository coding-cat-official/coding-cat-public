def check_id(l1, l2, target) -> bool:
    """
    Bug: Assumes both lists are of the same lentgh, could cause out of bounds error
    """
    for i, value in enumerate(l1):
        if value == target and l2[i] == target:
            return True
    return False

def check_same_identification_mutation(l1, l2, target) -> bool:
    """
    Bug: returns True or False only on the first run of the loop, poorly indented
    """
    for i, value in enumerate(l1):
        if i < len(l2) and value == target and l2[i] == target:
            return True
        return False

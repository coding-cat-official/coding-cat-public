def check_id(l1, l2, target) -> bool:
    for i, value in enumerate(l1):
        if i < len(l2) and value == target and l2[i] == target:
            return True
    return False

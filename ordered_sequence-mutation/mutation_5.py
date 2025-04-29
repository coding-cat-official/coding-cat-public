def ordered_sequence_mutation(nums):
    '''
    wrong logical operators
    '''
    for i in range(len(nums)-2):
        if nums[i] == 3 or nums[i+1] == 1 or nums[i+2] == 4:
            return True
    return False

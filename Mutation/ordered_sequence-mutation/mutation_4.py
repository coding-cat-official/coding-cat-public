def ordered_sequence_mutation(nums):
    '''
    forgot to add the range function
    '''
    for i in len(nums):
        if nums[i] == 3 and nums[i+1] == 1 and nums[i+2] == 4:
            return True
    return False

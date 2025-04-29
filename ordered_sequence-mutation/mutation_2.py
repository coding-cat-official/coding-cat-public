def ordered_sequence_mutation(nums):
    '''
    forgot a return statement
    '''
    for i in range(len(nums)-2):
        if nums[i] == 3 and nums[i+1] == 1 and nums[i+2] == 4:
            return True


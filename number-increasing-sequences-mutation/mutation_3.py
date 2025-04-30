def number_increasing_sequences_mutation(nums):
	'''
	Incorrectly decrease the initial count
	'''

	if len(nums) <= 1:
			return len(nums)
	
	increasing_sequences_count = 0 # decrease from 1 to 0
	for i in range(1, len(nums)):
		if nums[i-1] > nums[i]:
			increasing_sequences_count += 1

	return increasing_sequences_count
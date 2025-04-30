def number_increasing_sequences_mutation(nums):
	'''
	Correct implementation
	'''

	if len(nums) <= 1:
			return len(nums)
	
	increasing_sequences_count = 1
	for i in range(1, len(nums)):
		if nums[i-1] > nums[i]:
			increasing_sequences_count += 1

	return increasing_sequences_count
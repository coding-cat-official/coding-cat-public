def nbr_increasing_sequences(nums):
  '''
  Incorrectly shorten the range of numbers iterated on in the list
  '''

  if len(nums) <= 1:
      return len(nums)
  
  increasing_sequences_count = 1
  for i in range(2, len(nums)): # replace 1 with 2
    if nums[i-1] > nums[i]:
      increasing_sequences_count += 1

  return increasing_sequences_count
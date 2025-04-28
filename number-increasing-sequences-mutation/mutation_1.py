def nbr_increasing_sequences(nums):
  '''
  Wrong comparaison operator
  '''

  if len(nums) >= 1: # replace <= with >=
      return len(nums)
  
  increasing_sequences_count = 1
  for i in range(1, len(nums)):
    if nums[i-1] > nums[i]:
      increasing_sequences_count += 1

  return increasing_sequences_count
def sum_first_half(nums):
  '''
  Returning the spliced list in half instead of the sum of the spliced list
  '''
  if (len(nums))%2==0:
    middle=(len(nums))//2
  else:
      middle=(((len(nums))//2)+1)
  return (nums[:middle])#we forgot to use the sum on the half list
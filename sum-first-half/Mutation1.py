def sum_first_half(nums):
  '''
  inversed the odd and even operations
  '''
  if (len(nums))%2==1:#here we chose it to be odd instead of even
    middle=(len(nums))//2 # we are dividing by 2 and flooring it but not adding one because it is odd
  else:
      middle=(((len(nums))//2)+1)
  return [sum(nums[:middle])]
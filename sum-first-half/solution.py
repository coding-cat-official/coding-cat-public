def sum_first_half(nums):
    if (len(nums))%2==0:
        middle=(len(nums))//2
    else:
      middle=(((len(nums))//2)+1)
    return [sum(nums[:middle])]
def exponential_list_check(nums_list):
        """Returning True instead of False when the conditions for a non-exponential list are met"""
        for i in range(0, len(nums_list) - 1):
               if (nums_list[i] < nums_list[i + 1]) != True:
                      return True
        return True

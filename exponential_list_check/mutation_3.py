def exponential_list_check(nums_list):
        """Wrong condition check (False instead of True)"""
        for i in range(0, len(nums_list) - 1):
               if (nums_list[i] < nums_list[i + 1]) != False:
                      return False
        return True

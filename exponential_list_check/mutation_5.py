def exponential_list_check(nums_list):
        """Forgetting to return True when the list is exponential"""
        for i in range(0, len(nums_list) - 1):
               if (nums_list[i] < nums_list[i + 1]) != True:
                      return False

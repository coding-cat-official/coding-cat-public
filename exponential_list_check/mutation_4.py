def exponential_list_check(nums_list):
        """Inversing the number checks in the comparaison (switching [i+1] and [i]"""
        for i in range(0, len(nums_list) - 1):
               if (nums_list[i+1] < nums_list[i]) != True:
                      return False
        return True

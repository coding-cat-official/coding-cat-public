def list_match(list_1, list_2):
   '''
      count already has a starting value
   '''
   min_length = min(len(list_1), len(list_2))
   count = 1
   for i in range(min_length):
      if list_1[i] == list_2[i]:
         count += 1
   return count

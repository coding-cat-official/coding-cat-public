def list_match_mutation(list_1, list_2):
   '''
      checks how many NOT in list
   '''
   min_length = min(len(list_1), len(list_2))
   count = 0
   for i in range(min_length):
      if list_1[i] != list_2[i]:
         count += 1
   return count

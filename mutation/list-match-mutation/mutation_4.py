def list_match_mutation(list_1, list_2):
   '''
      does not compare at correct value
   '''
   min_length = min(len(list_1), len(list_2))
   count = 0
   for i in range(min_length):
      if list_1[i-1] == list_2[i]:
         count += 1
   return count

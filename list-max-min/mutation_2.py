def list_max_min(nums):
    '''
    By indenting the return inside the second if statement, one assumes all values go over 30, however this is False because some values can go exactly to 30 in which case the code will not return anything 
    '''
    l = []
    max_val = max(nums)
    min_val = min(nums)
    if max(nums) + min(nums)<=0:
        return 0
    while sum(l) < 30:
        l.append(max_val+min_val)
    if sum(l) > 30:
        l.remove(l[0])
        return l

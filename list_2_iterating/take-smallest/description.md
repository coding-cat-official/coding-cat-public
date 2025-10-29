Write a function `take_smallest(lst)` that takes a list of integers `lst` and removes the smallest element from the list. The function should return both the smallest element from the list *and* the modified list after removing that element. You can return two things in return statement by putting the outputs in a list, like `return [1, [4, 2, 3]]`)

You can NOT use Python's `min()` function. 


```python
take_smallest([4, 2, 3, 1])   # returns [1, [4, 2, 3]]
take_smallest([5, 1, 4, 2, 8]) # returns [1, [5, 4, 2, 8]]
take_smallest([3, 3, 1, 3])    # returns [1, [3, 3, 3]]
take_smallest([10])            # returns [10, []]
```

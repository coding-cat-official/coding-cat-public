**Before starting this problem, complete the Ordered Insert first! You will use that solution to
solve this one!**

In this problem, you will implement the *insertion sort* algorithm. You already implemented the bulk of this problem by writing the `ordered_insert` function!

To start, copy over your correct code for `ordered_insert` into the code editor.

Then, write a new function `insertion_sort(lst)`, which given an unordered list, will return the same list sorted. In the `insertion_sort` function, create a new empty list which we will copy values from the input list into. To do this, use a `while` loop to repeatedly call the `ordered_insert` function until all values from the input list are copied into the new list we created. `ordered_insert` will ensure when we add these new elements, they are in the correct placement! Recall, we stop this while loop when the original input list is empty from having the elements removed one-by-one.

- `insertion_sort([3, 2, 1])` returns `[1, 2, 3]`

**Before starting this problem, complete take_smallest first. You will use code in that problem to
solve this one!**

In this problem, you will implement the *selection sort* algorithm. You already implemented the bulk of this problem by writing the `take_smallest` function!

To start, copy over your correct code for `take_smallest` into the code editor.

Then, write a new function `selection_sort(lst)`, which given an unordered list, will return the same list sorted. In the `selection_sort` function, create a new empty list which we will copy values from the input list into. To do this, use a `while` loop to repeatedly call the `take_smallest` function. Recall, `take_smallest` will return the the smallest element of the list, removed from that list. Now we find and takes the smallest value one at a time and add it to our new list we constructed, until all values from the input list are moved into the new list we created. Recall, we stop this while loop when the original input list is empty from having the elements removed one-by-one.

Since `take_smallest` returns two things, the smallest element and the list with that element
removed, when we call this function we can assign both outputs to a variable immediately, like `x,
y = take_smallest(lst)`. The first element from the output is assigned to x, and the second element
is assigned to y.

- `selection_sort([3, 2, 1])` returns `[1, 2, 3]`

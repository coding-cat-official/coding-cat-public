If you want to combine and compare multiple conditions together, you're going to need the `and` and `or` logical operators.

Python has three logical operators for combining conditions:
- `and`: both sides must be `True`
- `or`: at least one side must be `True`
- `not`: flips `True` to `False` and vice versa (not used in this problem but good to know!)

Example:
```
True and False → False
True or False → True
not True → False
```

When mixing `and` and `or`, like when using PEMDAS, use parentheses to prioritize operations and make your intent clear. In the order or operations, `and` comes before `or`.

Example:
```
a = True
b = True
c = False
```


```
a or b and c
True or True and False
True or [True and False]  # 'and' evaluated first, True and False → False 
True or False
True
```
VS
```
(a or b) and c
(True or True) and False
[(True or True)] and False  # parentheses first, True or True → True
True and False
False
```
See how the parentheses affects the order of operations?


<hr/>

Write a function `check_venue_access(age, has_ticket, is_vip)` that returns `True` if a person can enter a venue, and `False` otherwise.
The function takes as input and `int` for the person's `age`, and two `bool`s for whether they have their ticket and if they are a VIP.
The rules are:
- They must be 18 or older *and* have their ticket
- *Or* they must be a VIP (VIPs always get in, no matter what)

For example:
- `check_venue_access(18, True, False)` → `True`
- `check_venue_access(20, False, False)` → `False`, they don't have their ticket
- `check_venue_access(16, False, True)` → `True`, while underage and without ticket, they are a VIP

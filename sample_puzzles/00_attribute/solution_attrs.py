# TITLE: 00_attribute >> solution_attrs.py
# AUTHOR: Chalmer Lowe
# DATE: 20181025
# DESCRIPTION:

# In this puzzle, you will be given a pickle file (object.p) that contains
#     a Python object based on a custom class called "obj". The Python object
#     has a wide variety of attributes.
#     Some of the attributes are labeled 'attr_' followed by a sequence of
#     numbers and/or letters. Each of these labeled attributes has a random
#     value associated with it (between [0, 5], including both end points).

# Open the file, read in the python object and parse the attributes associated
#     with the object. Determine the value associated with each object. Sum up
#     all the odd values.
#
# For example, given a Python object with these attributes and the associated
#     values:
# ATTRIBUTES         VALUES       COMMENT
# myobj.attr_0            0       # even
# myobj.attr_101b         2       # even
# myobj.attr_106f         1       # odd
# myobj.attr_25a          5       # odd
# myobj.attr_4d0          0       # even

# The answer is the sum of the two odd values:
#      1 + 5
# -----------
# Answer = 6

# NOTE: to unpickle an object based on a custom class, your script must
#     provide at least a dummy custom class with the same name so that pickle
#     can use it to write out the attributes, etc.

# ==============================================================
# Your code goes here:


# Solution 0 -----------------------

import pickle

class obj():
    pass

data = open('object.p', 'rb')

my_obj = pickle.load(data)

total = 0

for attr in dir(my_obj):
    if '__' not in attr:
       value = my_obj.__getattribute__(attr)

       if value % 2 == 1:
           total += value

print('Answer: {}'.format(total))

# Expected Answer: 1799870

# Solution 1 -----------------------

import pickle

class obj():
    pass

with open('object.p', 'rb') as data:
    my_obj = pickle.load(data)
    attr_values = [my_obj.__getattribute__(attr)
                   for attr in dir(my_obj) if '__' not in attr]
    odds = [num for num in attr_values if num % 2 == 1]

print('Answer: {}'.format(sum(odds)))

# Solution 2 ------------------------

import pickle

class obj():
    pass

with open('object.p', 'rb') as data:
    result = 0
    for i, a in enumerate([x for x in dir(my_obj) if '__' not in x]):
        value = my_obj.__getattribute__(a)
        if value % 2 == 1:
            result += value

print('Answer: {}'.format(result))

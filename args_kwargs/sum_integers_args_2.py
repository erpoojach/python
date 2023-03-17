# sum_integers_args_2.py
def my_sum(*integers):
    result = 0
    for x in integers:
        result += x
    return result

print(my_sum(1, 2, 3))

# change_list.py
my_list = [1, 2, 3]
my_list[0] = 9
print(my_list)

# change_tuple.py
my_tuple = (1, 2, 3)
#my_tuple[0] = 9
print(my_tuple)

# concatenate.py
def concatenate(**kwargs):
    result = ""
    # Iterating over the Python kwargs dictionary
    for arg in kwargs.values():
        result += arg
    return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))

# concatenate_2.py
def concatenate(**words):
    result = ""
    for arg in words.values():
        result += arg
    return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))

def concatenate_keys(**kwargs):
    result = ''
    for arg in kwargs:
        result += arg
    return result

print(concatenate_keys(a="Real", b="Python", c="Is", d="Great", e="!"))


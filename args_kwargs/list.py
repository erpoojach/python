# print_list.py
my_list = [1, 2, 3]
print(my_list)
#print_unpacked_list
print(my_list)

print(*my_list)
#print(**my_list)


# unpacking_call.py
def my_sum(a, b, c):
    print(a + b + c)

my_list = [1, 2, 3]
my_sum(*my_list)

# extract_list_body.py
my_list = [1, 2, 3, 4, 5, 6]

a, *b, c = my_list

print(a)
print(b)
print(c)

# merging_lists.py
my_first_list = [1, 2, 3]
my_second_list = [4, 5, 6]
my_merged_list = [*my_first_list, *my_second_list]

print(my_merged_list)

# merging_dicts.py
my_first_dict = {"A": 1, "B": 2}
my_second_dict = {"C": 3, "D": 4}
my_merged_dict = {**my_first_dict, **my_second_dict}

print(my_merged_dict)

# string_to_list.py
a = [*"RealPython"]
print(a)

# mysterious_statement.py
*a, = "RealPython"
print(a)

def concat(*args, sep="/"):
    return sep.join(args)

print(concat("earth", "mars", "venus"))

print(concat("earth", "mars", "venus", sep="."))

print(list(range(3, 6)))            # normal call with separate arguments

args = [3, 6]
print(list(range(*args)))          # call with arguments unpacked from a list
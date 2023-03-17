squares = [1, 4, 9, 16, 25]
print(squares)
print(squares[0]) # indexing returns the item
print(squares[-1])
print(squares[-3:])  # slicing returns a new list
print('Lists also support operations like concatenation:')
print(squares + [36, 49, 64, 81, 100])
#output - [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#Unlike strings, which are immutable, lists are a mutable type, i.e. it is possible to change their content:
cubes = [1, 8, 27, 65, 125]  # something's wrong here
print(cubes)
print(4 ** 3) # the cube of 4 is 64, not 65!
cubes[3] = 64 # replace the wrong value
print(cubes)
#You can also add new items at the end of the list, by using the append() method (we will see more about methods later):
cubes.append(216)  # add the cube of 6
print(cubes)
cubes.append(7 ** 3)  # and the cube of 7
print(cubes)
#[1, 8, 27, 64, 125, 216, 343]

#Assignment to slices is also possible, and this can even change the size of the list or clear it entirely:
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
# replace some values
letters[2:5] = ['C','D','E']
print(letters)
# now remove them
letters[2:5] = []
print(letters)
# clear the list by replacing all the elements with an empty list
letters[:] = []
print(letters)
letters = ['a', 'b', 'c', 'd']
print(len(letters))

#It is possible to nest lists (create lists containing other lists), for example:
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(a)
print(n)
print(x)
print(x[0])
print(x[0][1])
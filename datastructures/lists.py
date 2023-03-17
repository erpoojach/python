fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits)

print('count - ',fruits.count('orange'))
print('count - ',fruits.count('apple'))
print('count - ',fruits.count('tangerine'))
print('index - ',fruits.index('banana'))
print('index - ',fruits.index('banana',4)) # Find next banana starting a position 4

fruits.reverse()
print('reverse - ',fruits)

fruits.append('grape')
print(fruits)

fruits.sort()
print('sort - ',fruits)

fruits.pop()
print('pop - ',fruits)


print('using list as stack')
stack = [3, 4, 5]
stack.append(6)
print(stack)
stack.append(7)
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)

print('Using Lists as Queues')
from collections import deque
queue = deque(["Eric", "John", "Michael"])
print(queue)
queue.append("Terry")           # Terry arrives
print(queue)
queue.append("Graham")          # Graham arrives
print(queue)
queue.popleft()                 # The first to arrive now leaves
print(queue)
queue.popleft()                 # The second to arrive now leaves
print(queue)  # Remaining queue in order of arrival


print('list comprehension')

squares = []
for x in range(10):
    squares.append(x**2)

print(squares)

squares = list(map(lambda x: x**2, range(10)))
print(squares)

squares = [x**2 for x in range(10)]
print(squares)

#A list comprehension consists of brackets containing an expression followed by a for clause, 
# then zero or more for or if clauses. The result will be a new list resulting from evaluating the expression
#  in the context of the for and if clauses which follow it. For example, this listcomp combines the elements
#  of two lists if they are not equal:


print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])
print([(x, y) for x in [1,2,3] for y in [3,1,4]])


#and it’s equivalent to:

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

print(combs)


vec = [-4, -2, 0, 2, 4]
print(vec)
# create a new list with the values doubled
print([x*2 for x in vec])

# filter the list to exclude negative numbers
print([x for x in vec if x >= 0])

# apply a function to all the elements
print([abs(x) for x in vec])

# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit])

# create a list of 2-tuples like (number, square)
print([(x, x**2) for x in range(6)])

# the tuple must be parenthesized, otherwise an error is raised
#[x, x**2 for x in range(6)]
''' File "<stdin>", line 1
    [x, x**2 for x in range(6)]
     ^^^^^^^
SyntaxError: did you forget parentheses around the comprehension target?'''
# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
#The following list comprehension will transpose rows and columns:
print([[row[i] for row in matrix] for i in range(4)])

#Del 
#There is a way to remove an item from a list given its index instead of its value: the del statement. This differs from the pop() method which returns a value. The del statement can also be used to remove slices from a list or clear the entire list (which we did earlier by assignment of an empty list to the slice). For example:

a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
print(a[2:4])
del a[2:4]
print(a)

del a[:]
print(a)

print('-'*20)
t = 12345, 54321, 'hello!'
print(t[0])

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u)

# Tuples are immutable:
#t[0] = 88888
print(t)

# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
print(v)

print('-'*20)
empty = ()
singleton = 'hello',   # <-- note trailing comma
print(len(empty))

print(len(singleton))


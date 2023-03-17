class Base:
    a: int = 3
    b: str = 'abc'

class Derived(Base):
    pass

print(Derived.__annotations__)

#
def sum_two_numbers(a:int,b:str)->int:
    return a+b

print(sum_two_numbers(2,3))

k = sum(i*i for i in range(10))
print(k) 
food = 'qwerr tty'
print('------food-----')
for i in range(len(food)):
    print(food[i])


for io in food:
    print(io)

tax = 12.5 / 100
price = 100.50
print(price * tax)
print('C:\some\name')  # here \n means newline!
print(r'C:\some\name')  # note the r - raw strings  before the quote
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
print('Strings can be concatenated (glued together) with the + operator, and repeated with *:')
print(3 * 'un' + 'ium')  ## 3 times 'un', followed by 'ium'

print('Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.')
print('Py' 'thon')

print('This feature is particularly useful when you want to break long strings:')

text = ('Put several strings within parentheses '
         'to have them joined together.')

print(text)

prefix = 'Py'
#print(prefix 'thon') # can't concatenate a variable and a string literal
print(prefix)

print('if you want to concatenate variables or a variable and a literal, use +:')
print(prefix+'thon')
print(3*prefix)
print(3*'prefix')

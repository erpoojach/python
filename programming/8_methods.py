def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


#giving only the mandatory argument: 
#a = ask_ok('Do you really want to quit?')

#giving one of the optional arguments: 
#b = ask_ok('OK to overwrite the file?', 2)

#or even giving all arguments: 
#c = ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

#print(a,b,c)

#The default values are evaluated at the point of function definition in the defining scope, so that

i = 5

def f(arg=i):
    print(arg)

i = 6
f()
#will print 5.

#Important warning: The default value is evaluated only once. 
# This makes a difference when the default is a mutable object such as a list, dictionary, or 
# instances of most classes. For example, the following function accumulates the arguments passed
#  to it on subsequent calls:

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

#If you don’t want the default to be shared between subsequent calls, you can write the function like this instead:

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))


#Keyword arguments

#Functions can also be called using keyword arguments of the form kwarg=value. For instance, the following function:

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
#accepts one required argument (voltage) and three optional arguments (state, action, and type). This function can be called in any of the following ways:

print('output 1 ---------') 
parrot(1000)                                          # 1 positional argument
print('output 2 ---------')
parrot(voltage=1000)                                  # 1 keyword argument
print('output 3 ---------')
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
print('output 4 ---------')
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
print('output 5 ---------')
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
print('output 6 ---------')
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

#but all the following calls would be invalid:
#parrot()                     # required argument missing
#parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
#parrot(110, voltage=220)     # duplicate value for the same argument
#parrot(actor='John Cleese')  # unknown keyword argument

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
#It could be called like this:

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
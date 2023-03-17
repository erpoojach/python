#When a final formal parameter of the form **name is present, it receives a dictionary (see Mapping Types — dict) containing all keyword arguments except for those corresponding to a formal parameter. This may be combined with a formal parameter of the form *name (described in the next subsection) which receives a tuple containing the positional arguments beyond the formal parameter list. (*name must occur before **name.) For example, if we define a function like this:
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    print("-" * 40)
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

#Function Examples¶
#Consider the following example function definitions paying close attention to the markers / and *:
#The first function definition, standard_arg, the most familiar form, places no restrictions on the calling convention and arguments may be passed by position or keyword:
def standard_arg(arg): 
   print(arg)

standard_arg(2)
standard_arg(arg=2)

#The second function pos_only_arg is restricted to only use positional parameters as there is a / in the function definition:
def pos_only_arg(arg, /):
    print(arg)

pos_only_arg(1)
#pos_only_arg(arg=1)

#The third function kwd_only_args only allows keyword arguments as indicated by a * in the function definition:
def kwd_only_arg(*, arg):
    print(arg)

#kwd_only_arg(3)
kwd_only_arg(arg=3)

#And the last uses all three calling conventions in the same function definition:
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

#combined_example(1, 2, 3) #TypeError: combined_example() takes 2 positional arguments but 3 were given
combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)
#combined_example(pos_only=1, standard=2, kwd_only=3) #TypeError: combined_example() got some positional-only arguments passed as keyword arguments: 'pos_only'

#Finally, consider this function definition which has a potential collision between the positional argument name and **kwds which has name as a key:

#def foo(name, **kwds):  #this will not work
def foo(xyz, **kwds):
    return 'name' in kwds

#There is no possible call that will make it return True as the keyword 'name' will always bind to the first parameter. For example:

print(foo(1, **{'name': 2}))

#But using / (positional only arguments), it is possible since it allows name as a positional argument and 'name' as a key in the keyword arguments:

def foo(name, /, **kwds):
    return 'name' in kwds
#In other words, the names of positional-only parameters can be used in **kwds without ambiguity.
print(foo(1, **{'name': 2}))



def gadgets_price(**kwargs):
   print(kwargs,type(kwargs))
gadgets_price(laptop= 60000, smartphone=10000, earphones =500)


def multiply(*args):
   x = 1
   for i in args:
      x = x * i
   print ('The product of the numbers is:',x)
multiply(2,2,2)
multiply(2,2)
multiply(3*2)
multiply(2,11)
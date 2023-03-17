#while True print('Hello world')
i = 0
while (i<5): 
        print('Hello world')
        i+=1

#the types in the example are ZeroDivisionError, NameError and TypeError.
'''
Traceback (most recent call last):
  File "C:\xamp\htdocs\pythonproject\scripts\errors_n_exceptions\syntax_error.py", line 7, in <module>
    print(10 * (1/0))
'''
#print(10 * (1/0))

'''Traceback (most recent call last):
  File "C:\xamp\htdocs\pythonproject\scripts\errors_n_exceptions\syntax_error.py", line 10, in <module>
    print(4 + spam*3)
              ^^^^
NameError: name 'spam' is not defined'''
#print(4 + spam*3)

'''Traceback (most recent call last):
  File "C:\xamp\htdocs\pythonproject\scripts\errors_n_exceptions\syntax_error.py", line 13, in <module>
    print('2' + 2)
          ~~~~^~~
TypeError: can only concatenate str (not "int") to str'''
#print('2' + 2)


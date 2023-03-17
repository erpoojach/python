tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)

tel['jack']
print(tel)
del tel['sape']
tel['irv'] = 4127
print(tel)

list(tel)
print(tel)
sorted(tel)
print(tel)
print('guido' in tel)

print('jack' not in tel)

print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])) #The dict() constructor builds dictionaries directly from sequences of key-value pairs:

#In addition, dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:

print({x: x**2 for x in (2, 4, 6)})
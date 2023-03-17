word = 'Python'
print(word[0],word[5])
#P n
print(word[-1],word[-6]) #Note that since -0 is the same as 0, negative indices start from -1.
#n P
print(word[2:5])
#tho
print(word[0:2])
#Py
print(word[:3])
#Pyt

print(word[0:2]) # characters from position 0 (included) to 2 (excluded)
#'Py'
print(word[2:5])  # characters from position 2 (included) to 5 (excluded)
#'tho'
print(word[:2])  # character from the beginning to position 2 (excluded)
#'Py'
print(word[4:])   # characters from position 4 (included) to the end
#'on'
print(word[-2:]) # characters from the second-last (included) to the end
#'on'
print('Note how the start is always included, and the end always excluded. This makes sure that s[:i] + s[i:] is always equal to s:')

print(word[:2] + word[2:])
#'Python'
print( word[:4] + word[4:])
#'Python'
#word[0] = 'J' Python strings cannot be changed — they are immutable. Therefore, assigning to an indexed position in the string results in an error:
print(word)

print('The built-in function len() returns the length of a string:')
s = 'pooja'
print(len(s))
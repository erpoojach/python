#Creating a list which contains name of Indian cities  

cities = ['Delhi', 'Mumbai', 'Kolkata']
# Printing the elements from the list cities, separated by a comma & space

for city in cities:
	print(city, end=',')

#Printing the location of the object created in the memory address in hexadecimal format

print(hex(id(cities)))
#Adding a new city to the list cities

cities.append('Chennai')
#Printing the elements from the list cities, separated by a comma & space 

for city in cities:
	print(city, end=',')
#Printing the location of the object created in the memory address in hexadecimal format

print(hex(id(cities)))

#The above example shows us that we were able to change the internal state of the object ‘cities’
#  by adding one more city ‘Chennai’ to it, yet, the memory address of the object did not change. 
# This confirms that we did not create a new object, rather, the same object was changed or mutated. 
# Hence, we can say that the object which is a type of list with reference variable name ‘cities’ is a MUTABLE OBJECT.

print('/n------------------immutable--------------------')

#Creating a Tuple with variable name ‘foo’

foo = (1, 2)
#Changing the index[0] value from 1 to 3
print(foo)
#foo[0] = 3
	
#TypeError: 'tuple' object does not support item assignment 

#creating a tuple (immutable object) which contains 2 lists(mutable) as it’s elements
#The elements (lists) contains the name, age & gender 
person = (['Ayaan', 5, 'Male'], ['Aaradhya', 8, 'Female'])
#printing the tuple

print(person)
#printing the location of the object created in the memory address in hexadecimal format

print(hex(id(person)))
#Changing the age for the 1st element. Selecting 1st element of tuple by using indexing [0] then 2nd element of the list by using indexing [1] and assigning a new value for age as 4

person[0][1] = 4
#printing the updated tuple

print(person)
print(hex(id(person)))

#creating a list (mutable object) which contains tuples(immutable) as it’s elements

list1 = [(1, 2, 3), (4, 5, 6)]
print(list1)
#printing the location of the object created in the memory address in hexadecimal format
print(hex(id(list1)))

#changing object reference at index 0
list1[0] = (7, 8, 9)
#printing the list
print(list1)
print(hex(id(list1)))


x = 10
print(x)
print(hex(id(x)))
y = 10
print(y)
print(hex(id(y)))


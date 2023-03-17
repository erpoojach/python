#5.6. Looping Techniques
#When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the items() method.


knights = {'Pooja': 'Q3', 'Rohit': 'PI', 'Anju':'ITC'}
for k, v in knights.items():
    print(k,'------', v)

for k in knights:
    print(k,'------')
    
#When looping through a sequence, the position index and corresponding value can be retrieved at the same time using the enumerate() function.

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

#To loop over two or more sequences at the same time, the entries can be paired with the zip() function.

questions = ['Name', 'Company', 'Favorite color']
answers = ['Pooja', 'PIQ3', 'Yellow']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

#To loop over a sequence in reverse, first specify the sequence in a forward direction and then call the reversed() function.
for i in reversed(range(1, 10, 2)):
     print(i)
print('----------')
for i in reversed(range(1, 10)):
     print(i)
print('----------')
#To loop over a sequence in sorted order, use the sorted() function which returns a new sorted list while leaving the source unaltered.
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)
print('----------')
for i in basket:
    print(i)

print('----set--------')
#Using set() on a sequence eliminates duplicate elements. The use of sorted() in combination with set() over a sequence is an idiomatic way to loop over unique elements of the sequence in sorted order.
for f in sorted(set(basket)):
    print(f)
print('------------')
for f in set(basket):
    print(f)
print('-----More on Conditions-------')

string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)

#------------------------
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#------------------------------
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#--------Loop through the letters in the word "banana":---------------
for x in "banana":
  print(x)
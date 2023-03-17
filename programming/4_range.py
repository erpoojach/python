for i in range(5):
    print(i)

print(list(range(5, 50)))

print(list(range(5, 50, 5)))

print(list(range(-5, -50, -5)))

#To iterate over the indices of a sequence, you can combine range() and len() as follows:
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
 print(i, a[i], len(a))


print(range(4))
print(sum(range(4)))